import socket

def detect_service(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))

        if port in (80, 8080, 443):
            sock.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        else:
            sock.send(b"\r\n")

        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()

        return banner if banner else None
    except Exception:
        return None
