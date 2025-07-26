import logging
import json
from scapy.layers.inet import IP, TCP, UDP, ICMP

with open("rules.json") as f:
    RULES = json.load(f)

logging.basicConfig(filename="logs/firewall.log", level=logging.INFO, format='%(asctime)s - %(message)s')

def packet_filter(packet):
    if IP in packet:
        ip_src = packet[IP].src

        # Check blocked IPs
        if ip_src in RULES["blocked_ips"]:
            logging.info(f"Blocked IP: {ip_src}")
            return

        # Check blocked ports
        if TCP in packet or UDP in packet:
            port = packet[TCP].sport if TCP in packet else packet[UDP].sport
            if port in RULES["blocked_ports"]:
                logging.info(f"Blocked Port: {port} from {ip_src}")
                return

        # Check blocked protocols
        if ICMP in packet and "ICMP" in RULES["blocked_protocols"]:
            logging.info(f"Blocked ICMP packet from: {ip_src}")
            return

        # If none blocked, log as allowed
        logging.info(f"Allowed Packet: {ip_src}")
