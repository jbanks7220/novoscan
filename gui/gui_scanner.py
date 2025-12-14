from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLineEdit,
    QLabel, QFileDialog, QProgressBar, QComboBox
)
from PyQt5.QtCore import QTimer

from scanner.safe_scan import run_safe_scan
from exporter.exporter import export_report


# =========================
# Dark UI Theme
# =========================
DARK_STYLE = """
QWidget {
    background-color: #0b0b0d;
    color: #e6e6eb;
    font-family: Consolas;
    font-size: 13px;
}
QLineEdit, QComboBox {
    background-color: #2b2b30;
    border: 1px solid #6d3cff;
    padding: 6px;
}
QPushButton {
    background-color: #6d3cff;
    border-radius: 4px;
    padding: 8px;
    color: white;
}
QPushButton:hover {
    background-color: #8457ff;
}
QTextEdit {
    background-color: #111114;
    border: 1px solid #2f2f33;
}
QProgressBar {
    background-color: #1c1c22;
    border: 1px solid #2f2f33;
    height: 16px;
}
QProgressBar::chunk {
    background-color: #6d3cff;
}
"""


# =========================
# Fake Terminal Output
# =========================
FAKE_TERMINAL_LINES = [
    "[*] Initializing NovoScan core modules...",
    "[*] Loading attack surface definitions...",
    "[*] Enumerating exposed services...",
    "[*] Fingerprinting service versions...",
    "[*] Correlating weaknesses...",
    "[*] Mapping MITRE ATT&CK techniques...",
    "[*] Constructing attack chains...",
    "[*] Calculating risk scores..."
]


# =========================
# Main GUI
# =========================
class ScannerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("NovoScan – Attack Surface Analyzer")
        self.setMinimumSize(900, 650)
        self.setStyleSheet(DARK_STYLE)

        self.results = None
        self.fake_index = 0

        # ---------------------
        # Layout
        # ---------------------
        layout = QVBoxLayout()

        self.target = QLineEdit()
        self.target.setPlaceholderText("Target IP or Hostname")

        self.profile = QComboBox()
        self.profile.addItems(["quick", "stealth", "full"])

        self.scan_btn = QPushButton("Start Scan")
        self.scan_btn.clicked.connect(self.start_scan)

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        # Export buttons
        export_layout = QHBoxLayout()
        self.btn_html = QPushButton("Export HTML")
        self.btn_json = QPushButton("Export JSON")
        self.btn_md = QPushButton("Export Markdown")
        self.btn_xml = QPushButton("Export XML")

        for b in (self.btn_html, self.btn_json, self.btn_md, self.btn_xml):
            b.setEnabled(False)
            export_layout.addWidget(b)

        self.btn_html.clicked.connect(lambda: self.export("html"))
        self.btn_json.clicked.connect(lambda: self.export("json"))
        self.btn_md.clicked.connect(lambda: self.export("md"))
        self.btn_xml.clicked.connect(lambda: self.export("xml"))

        # Assemble layout
        layout.addWidget(QLabel("Target"))
        layout.addWidget(self.target)
        layout.addWidget(QLabel("Scan Profile"))
        layout.addWidget(self.profile)
        layout.addWidget(self.scan_btn)
        layout.addWidget(self.progress)
        layout.addWidget(self.output)
        layout.addLayout(export_layout)

        self.setLayout(layout)

        # Fake scan timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.fake_scan_step)

    # =========================
    # Scan Flow
    # =========================
    def start_scan(self):
        target = self.target.text().strip()
        if not target:
            return

        self.results = None
        self.fake_index = 0
        self.progress.setValue(0)
        self.output.clear()

        self.scan_btn.setEnabled(False)
        for b in (self.btn_html, self.btn_json, self.btn_md, self.btn_xml):
            b.setEnabled(False)

        profile = self.profile.currentText()
        self.output.append(f"[+] NovoScan started ({profile.upper()} scan)\n")

        self.timer.start(600)

    def fake_scan_step(self):
        if self.fake_index < len(FAKE_TERMINAL_LINES):
            self.output.append(FAKE_TERMINAL_LINES[self.fake_index])
            self.fake_index += 1
            self.progress.setValue(int((self.fake_index / len(FAKE_TERMINAL_LINES)) * 80))
        else:
            self.timer.stop()
            self.progress.setValue(90)
            self.output.append("\n[*] Executing vulnerability analysis...\n")
            self.run_real_scan()

    def run_real_scan(self):
        target = self.target.text().strip()
        profile = self.profile.currentText()

        self.results = run_safe_scan(target, profile)

        # ---------------------
        # Vulnerabilities
        # ---------------------
        self.output.append("=== Vulnerabilities ===")
        for v in self.results.get("vulnerabilities", []):
            self.output.append(
                f"- {v['name']} ({v['severity']})\n"
                f"  Port: {v['port']} | Service: {v['service']}\n"
                f"  Impact: {v['impact']}\n"
                f"  MITRE: {', '.join(v['mitre'])}\n"
            )

        # ---------------------
        # Attack Chains
        # ---------------------
        self.output.append("\n=== Attack Chains ===")
        for c in self.results.get("attack_chains", []):
            self.output.append(f"- {c['name']} ({c['severity']})")
            for step in c.get("steps", []):
                self.output.append(f"    • {step}")
            self.output.append("")

        self.progress.setValue(100)
        self.output.append("[✓] Scan complete")

        self.scan_btn.setEnabled(True)
        for b in (self.btn_html, self.btn_json, self.btn_md, self.btn_xml):
            b.setEnabled(True)

    # =========================
    # Export
    # =========================
    def export(self, fmt):
        if not self.results:
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Report",
            f"novoscan_report.{fmt}",
            f"*.{fmt}"
        )

        if path:
            export_report(self.results, path)
