## 🔥 Personal Firewall using Python (Kali Linux)

A lightweight and customizable personal firewall built with Python, capable of monitoring, filtering, and logging network traffic in real-time. It uses `scapy` for packet sniffing, `iptables` for system-level enforcement, and `Tkinter` for a user-friendly GUI.

## 🎯 Objective

To develop a personal firewall that:
- Filters incoming/outgoing packets based on user-defined rules (IP, port, protocol)
- Provides both CLI and GUI interfaces for user control
- Logs all network activity (allowed/blocked) for audit and debugging

## 🛠 Tools & Technologies

- **Python** – Core scripting language
- **Scapy** – Packet sniffing and parsing
- **iptables** – Linux-based system firewall integration
- **Tkinter** – GUI for starting/stopping and viewing logs
- **Kali Linux** – Development and testing environment

## 🚀 Features

- Monitor traffic in real-time using `scapy`
- Block or allow packets based on:
  - IP addresses
  - Port numbers
  - Protocols (TCP, UDP, ICMP)
- Persistent logging of all network activity
- Easy customization via `rules.json` file
- GUI with live log display and firewall controls


## ✅ Deliverables

-  CLI or GUI-based firewall
-  Custom rule definition
-  Real-time traffic monitoring
-  Persistent logging

## 🧪 Tested On

- **OS**: Kali Linux
- **Python Version**: 3.8+
- **Privileges**: Requires root for packet sniffing and iptables access

## 📎 Future Enhancements

- Email alerts on suspicious activity
- Web-based dashboard for remote management
- Integration with threat intelligence APIs

---

🔐 Built with love and a strong focus on cybersecurity. Contributions and feedback are welcome!


