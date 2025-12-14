def check_vulnerabilities(port, service=None):
    vulns = []

    def add(name, severity, desc, owasp, mitre, impact):
        vulns.append({
            "name": name,
            "severity": severity,
            "description": desc,
            "owasp": owasp,
            "mitre": mitre,
            "impact": impact,
            "port": port,
            "service": service or "unknown"
        })

    if port == 21:
        add(
            "Insecure FTP Service",
            "High",
            "FTP transmits credentials in plaintext.",
            "A2",
            ["T1046"],
            "Credential theft and lateral movement"
        )

    if port == 22:
        add(
            "SSH Service Exposed",
            "Medium",
            "SSH accessible from network.",
            "A2",
            ["T1021"],
            "Remote access brute force"
        )

    if port in (80, 8080):
        add(
            "Unencrypted HTTP Service",
            "Medium",
            "HTTP traffic is unencrypted.",
            "A2",
            ["T1046"],
            "Traffic interception and session hijacking"
        )

    if port == 3306:
        add(
            "MySQL Exposed",
            "High",
            "Database exposed to network.",
            "A5",
            ["T1078"],
            "Data exfiltration"
        )

    if port == 5432:
        add(
            "PostgreSQL Exposed",
            "High",
            "Database exposed to network.",
            "A5",
            ["T1078"],
            "Data exfiltration"
        )

    if port == 27017:
        add(
            "MongoDB Exposed",
            "Critical",
            "MongoDB often exposed without authentication.",
            "A5",
            ["T1078"],
            "Complete database compromise"
        )

    return vulns
