# Fake Free Fire Diamond Hack Tool (Root Phone Required - Prank Only)
# HACKING WORLD™ - VIP EDITION
# ⚠️ This is 100% FAKE/PRANK tool for show-off purpose only.

import os
import time
import random

# Colors
G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
P = '\033[95m'
W = '\033[1;37m'

def clear():
    os.system("clear")

def banner():
    clear()
    print(f"""{G}
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║ ██╔╝██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
█████╔╝ ███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██╗██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
        {Y}HACKING WORLD™ - DIAMOND VIP TOOL
           {R}WORKS ON ROOT DEVICES ONLY
{W}---------------------------------------------------
""")

def check_root():
    print(f"{C}[✓] Checking Root Access...")
    time.sleep(2)
    if os.path.exists("/system/bin/su") or os.path.exists("/system/xbin/su"):
        print(f"{G}[✓] Root Access Detected!\n")
        return True
    else:
        print(f"{R}[✘] Root Access Not Found!")
        print(f"{Y}[!] This tool only works on ROOTED devices.")
        input(f"\n{W}Press Enter to Exit...")
        exit()

def loading(text, sec):
    for i in range(sec):
        print(f"{C}{text}{'.' * (i%4)}", end='\r')
        time.sleep(1)

def hack_menu():
    banner()
    print(f"{W}[1] Start Diamond Hack")
    print(f"{W}[0] Exit\n")
    choice = input(f"{Y}[?] Choose Option: {W}")
    if choice == '1':
        diamond_hack()
    else:
        print(f"{R}Exiting...")
        time.sleep(1)
        exit()

def diamond_hack():
    banner()
    check_root()
    uid = input(f"{C}Enter Free Fire UID: {W}")
    print()
    loading("Connecting to Free Fire Secure Server", 3)
    print(f"{G}[✓] UID Verified: {uid}")
    time.sleep(1.5)
    print(f"{Y}[+] Selecting VIP Diamond Packages...")
    time.sleep(2)
    
    diamonds = [500, 1000, 2000, 5200, 10000]
    for d in diamonds:
        print(f"{C}[*] Injecting {d} Diamonds...")
        time.sleep(1.5)

    print(f"\n{P}[✓] Finalizing Injection...")
    loading("Injecting Anti-Ban Patch", 3)

    # Fake issue simulation
    print(f"\n{R}[!] Error: Device Configuration Mismatch!")
    print(f"{Y}→ Device Android Version: 13 or Higher Required")
    print(f"{Y}→ Root Permission Failed")
    time.sleep(2)

    print(f"\n{R}⚠️ Injection Failed due to missing root access.")
    print(f"{C}Please try on a properly rooted device.")

    input(f"\n{W}Press Enter to Exit...")
    exit()

if __name__ == "__main__":
    hack_menu()