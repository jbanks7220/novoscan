import socket


def scan_ports(target, ports):
    """
    Scan a list of ports and return open ones.
    """
    open_ports = []

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return open_ports

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)

            sock.close()
        except Exception:
            continue

    return open_ports
