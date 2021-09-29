import tkinter as tk
import socket
import uuid
from getmac import get_mac_address
from tkinter import messagebox 
 
root = tk.Tk()
root.withdraw()
def get_Host_name_IP_MAC():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        mac = ':'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
        messagebox.showinfo("..::Network Finder by nikkpap @ 2021 ::..", "\n".join(["Hostname : ",host_name,"\n","IP Address : ",host_ip,"\n","MAC Address : ",mac]))
    except:
        messagebox.showerror("Error!", "Unable to get Hostname or IP or MAC")
   
get_Host_name_IP_MAC()
