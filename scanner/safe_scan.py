from scanner.port_scanner import scan_ports
from scanner.vuln_checks import check_vulnerabilities
from scanner.attack_mapper import build_attack_chains
from utils.helpers import detect_service


def run_safe_scan(target, profile="quick"):
    # Scan profiles
    if profile == "quick":
        ports = [21, 22, 80, 443, 3306, 5432]
    elif profile == "stealth":
        ports = [22, 80, 443]
    else:  # full
        ports = list(range(1, 1025))

    vulnerabilities = []

    open_ports = scan_ports(target, ports)

    print("[DEBUG] Open ports:", open_ports)

    for port in open_ports:
        service = detect_service(target, port)

        print(f"[DEBUG] Scanning port {port} ({service})")

        vulns = check_vulnerabilities(port)

        print(f"[DEBUG] Vulnerabilities found:", vulns)

        for v in vulns:
            v["port"] = port
            v["service"] = service
            vulnerabilities.append(v)

    attack_chains = build_attack_chains(vulnerabilities)

    print("[DEBUG] Attack chains:", attack_chains)

    return {
        "vulnerabilities": vulnerabilities,
        "attack_chains": attack_chains
    }
