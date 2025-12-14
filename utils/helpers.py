import socket

def detect_service(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()

        if "Apache" in banner:
            return "Apache"
        if "OpenSSH" in banner:
            return "OpenSSH"
        if "MySQL" in banner:
            return "MySQL"
        return "Unknown"
    except:
        return "Unknown"
