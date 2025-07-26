from scapy.all import sniff
from firewall_rules import packet_filter
from iptables_rules import apply_iptables_rules

def monitor_traffic():
    sniff(prn=packet_filter, store=False)

if __name__ == "__main__":
    apply_iptables_rules()
    monitor_traffic()
