OWASP_MAP = {
    "SQL Injection": "A03:2021 – Injection",
    "XSS": "A03:2021 – Injection",
    "Outdated Service": "A06:2021 – Vulnerable Components",
    "Database Exposure": "A02:2021 – Cryptographic Failures"
}

def map_owasp(vuln):
    return OWASP_MAP.get(vuln, "A05:2021 – Security Misconfiguration")
