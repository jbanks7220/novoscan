.

# 🛡️ NovoScan – Context-Aware Attack Surface Analyzer

NovoScan is a context-aware vulnerability scanner and attack surface analyzer that goes beyond traditional port scanning by correlating exposed services, vulnerabilities, and realistic attack chains using MITRE ATT&CK mappings.

Unlike simple Nmap wrappers, NovoScan focuses on how an attacker would actually move through a system — making it ideal for blue teamers, red teamers, students, and security engineers building real-world tooling.

## ✨ Key Features

## 🔍 Context-Aware Scanning

Identifies exposed services (SSH, HTTP, MySQL, PostgreSQL, FTP, etc.)

Associates vulnerabilities with realistic attacker impact

Service-aware findings instead of raw open ports

## 🧠 Attack Surface Mapping (Resume-Grade Feature)

Automatically builds multi-step attack chains

Correlates vulnerabilities into realistic exploitation paths

Mapped to MITRE ATT&CK techniques

Highlights critical compromise scenarios (credential reuse, lateral movement, data exfiltration)

## ⚡ Scan Profiles
Profile	Description
Quick	High-value ports for fast triage
Stealth	Low-noise footprint
Full	Comprehensive scan (1–1024)

## 🎨 Dark Hacker-Style GUI

Black / purple / Nardo gray theme

Simulated terminal output (movie-style scanning)

Live progress bar

Clean, readable results display

## 📄 Professional Report Exporting

HTML

JSON

Markdown

XML

Perfect for:

Documentation

Portfolio artifacts

Security assessments

## 🖥️ GUI Preview (Concept)

```
[+] NovoScan started (QUICK scan)
[*] Enumerating exposed services...
[*] Fingerprinting service versions...
[*] Mapping MITRE ATT&CK techniques...

=== Vulnerabilities ===
- SSH Service Exposed (Medium)
  Port: 22 | Service: OpenSSH
  Impact: Remote access brute force

=== Attack Chains ===
- Credential Reuse → Database Compromise (Critical)

```

## 🧱 Architecture Overview

```
novoscan-vuln-scanner/
│
├── main.py                 # Application entry point
├──data
|   └── novoscan.db
├──reports
|   ├── example_report.html # Example Report Syntax 
|   ├── example_report.json
|   ├── example_report.md
|   └── example_report.xml
├──tests
|   └── test_scanner.py     # Test script for port scanning
├── gui/
│   └── gui_scanner.py      # PyQt5 GUI
│
├── scanner/
│   ├── port_scanner.py     # TCP port scanning
│   ├── safe_scan.py        # Core scan orchestration
│   ├── vuln_checks.py      # Vulnerability logic
│   └── attack_mapper.py    # Attack chain generation
│
├── exporter/
│   └── exporter.py         # Report export engine
│
├── utils/
│   └── helpers.py          # Service detection helpers
│
└── README.md

```

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```
git clone https://github.com/jbanks7220/novoscan-vuln-scanner.git
cd novoscan-vuln-scanner

```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate  # Windows 
```
 OR
```
python -m venv venv
source venv/bin/activate # linux
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run NovoScan
```
python main.py
```
## 🎥 Video Demo

https://github.com/user-attachments/assets/4b551c2a-8f11-43d3-8547-797e5e7ea42e

## 🧪 Example Use Cases

Attack surface discovery for labs and homelabs

Blue team exposure analysis

Red team reconnaissance simulation

Cybersecurity portfolio project

Educational MITRE ATT&CK mapping

## ⚠️ Legal & Ethical Notice

NovoScan is intended for educational and authorized security testing only.

# ❌ Do NOT scan:

## Networks you do not own

## Systems without explicit permission

# You are responsible for complying with all applicable laws.

## 🧭 Roadmap (Future Enhancements)

CVE enrichment (NVD integration)

Risk scoring & prioritization

Kill-chain visualization

PDF executive reports

Plugin system for custom checks

## 👨‍💻 Author

Built by Jamir Banks

Navy veteran & former CTR | Cybersecurity hobbyist | Signals intelligence & secure comms background | Focused on defense, recon & red team skills

If you’re a recruiter:

This project demonstrates system design, security knowledge, and real-world attacker modeling — not just scripting.

## ⭐ Why NovoScan Stands Out

✅ Not just port scanning
✅ Context-aware analysis
✅ MITRE ATT&CK correlation
✅ Attack-chain reasoning
✅ Clean, professional GUI

This is not an Nmap clone.
