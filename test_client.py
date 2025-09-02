from firewall import Firewall

def main():
    fw = Firewall()

    # Simulate different client requests
    clients = [
        ("192.168.1.5", 22),   # Blocked IP
        ("192.168.1.10", 21),  # Blocked Port
        ("8.8.8.8", 80),       # Allowed
        ("10.0.0.100", 443),   # Blocked IP
        ("172.16.0.2", 23),    # Blocked Port
        ("192.168.1.15", 443)  # Allowed
    ]

    for ip, port in clients:
        fw.handle_request(ip, port)

if __name__ == "__main__":
    main()
