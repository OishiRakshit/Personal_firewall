import tkinter as tk
from tkinter import messagebox, scrolledtext
from threading import Thread
from firewall import monitor_traffic
from iptables_rules import apply_iptables_rules, flush_iptables_rules
import os
import signal

LOG_FILE = "logs/firewall.log"
firewall_thread = None
firewall_running = False

def start_firewall():
    global firewall_thread, firewall_running
    if not firewall_running:
        apply_iptables_rules()
        firewall_thread = Thread(target=monitor_traffic, daemon=True)
        firewall_thread.start()
        firewall_running = True
        messagebox.showinfo("Firewall", "Firewall started.")
    else:
        messagebox.showinfo("Firewall", "Firewall is already running.")

def stop_firewall():
    global firewall_running
    if firewall_running:
        flush_iptables_rules()
        os.kill(os.getpid(), signal.SIGTERM)  # stop sniffing by killing main thread
    else:
        messagebox.showinfo("Firewall", "Firewall is not running.")

def clear_logs():
    if os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()
    update_log_display()
    messagebox.showinfo("Logs", "Firewall logs cleared.")

def update_log_display():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            lines.reverse()  # Show newest logs at the top
            log_content = ''.join(lines)
            log_area.config(state='normal')
            log_area.delete(1.0, tk.END)
            log_area.insert(tk.END, log_content)
            log_area.config(state='disabled')
    root.after(2000, update_log_display)


# GUI Setup
root = tk.Tk()
root.title("Personal Python Firewall")
root.geometry("750x500")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start Firewall", command=start_firewall, bg="green", fg="white", width=20)
start_button.grid(row=0, column=0, padx=5)

stop_button = tk.Button(button_frame, text="Stop Firewall", command=stop_firewall, bg="orange", fg="white", width=20)
stop_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Logs", command=clear_logs, bg="red", fg="white", width=20)
clear_button.grid(row=0, column=2, padx=5)

log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20, state='disabled')
log_area.pack(padx=10, pady=10)

update_log_display()
root.mainloop()
