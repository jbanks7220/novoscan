from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer

class Splash(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background:#0b0b0d;color:#6d3cff;font-size:24px;")
        self.label = QLabel("NovoScan Initializing...", self)
        self.label.move(80, 80)
        self.setFixedSize(300,200)
        QTimer.singleShot(2000, self.close)
