import json

class Firewall:
    def __init__(self, rules_file="rules.json"):
        with open(rules_file, "r") as f:
            self.rules = json.load(f)

    def is_blocked(self, ip, port):
        """Check if traffic from given IP and port should be blocked."""
        if ip in self.rules["blocked_ips"]:
            return True
        if port in self.rules["blocked_ports"]:
            return True
        return False

    def handle_request(self, ip, port):
        """Simulate handling of incoming traffic."""
        if self.is_blocked(ip, port):
            print(f"🚫 Blocked traffic from {ip}:{port}")
        else:
            print(f"✅ Allowed traffic from {ip}:{port}")


if __name__ == "__main__":
    fw = Firewall()

    # Example test traffic
    test_requests = [
        ("192.168.1.5", 80),
        ("192.168.1.10", 21),
        ("10.0.0.2", 443),
        ("172.16.0.5", 22)
    ]

    for ip, port in test_requests:
        fw.handle_request(ip, port)
