import json
import os

def apply_iptables_rules():
    with open("rules.json") as f:
        rules = json.load(f)

    for ip in rules.get("blocked_ips", []):
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")

    for port in rules.get("blocked_ports", []):
        os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")
        os.system(f"sudo iptables -A INPUT -p udp --dport {port} -j DROP")

    if "ICMP" in rules.get("blocked_protocols", []):
        os.system("sudo iptables -A INPUT -p icmp -j DROP")

def flush_iptables_rules():
    os.system("sudo iptables -F")
