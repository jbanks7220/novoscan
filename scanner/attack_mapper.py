def build_attack_chains(vulnerabilities):
    """
    Build realistic attack chains from discovered vulnerabilities
    """

    chains = []
    ports = {v["port"] for v in vulnerabilities}

    # SSH + Database = credential reuse
    if 22 in ports and 3306 in ports:
        chains.append({
            "name": "Credential Reuse → Database Compromise",
            "severity": "Critical",
            "steps": [
                "Obtain SSH credentials via brute force or reuse",
                "Reuse credentials against MySQL service",
                "Dump sensitive database contents"
            ],
            "mitre": ["T1110", "T1078", "T1046"]
        })

    # Web → SSH pivot
    if 80 in ports and 22 in ports:
        chains.append({
            "name": "Web Foothold → SSH Lateral Movement",
            "severity": "High",
            "steps": [
                "Exploit web vulnerability",
                "Upload web shell",
                "Pivot to SSH for persistent access"
            ],
            "mitre": ["T1190", "T1059", "T1021"]
        })

    # Public DB exposure
    if 3306 in ports or 5432 in ports:
        chains.append({
            "name": "Exposed Database → Data Exfiltration",
            "severity": "Critical",
            "steps": [
                "Identify exposed database service",
                "Connect without authentication",
                "Exfiltrate sensitive records"
            ],
            "mitre": ["T1046", "T1005", "T1020"]
        })

    return chains
