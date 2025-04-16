import time
import sys
import random
import os
from tqdm import tqdm
import pyfiglet
from termcolor import colored
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Print the SEC Banner
def print_logo():
    os.system("cls" if os.name == "nt" else "clear")
    banner = pyfiglet.figlet_format("SEC PROTECTION", font="slant")
    print(colored(banner, "red"))
    print(Fore.CYAN + "══════════════════════════════════════════════════")
    print(Fore.RED + "        🔐 Ultimate Security by SEC Company 🔐")
    print(Fore.CYAN + "══════════════════════════════════════════════════\n")
    time.sleep(1)

# Print colored text
def print_colored(text, color):
    print(colored(text, color))

# Simulate a fake but fancy installation process
def fake_installation():
    steps = [
        "🔍 Scanning system vulnerabilities...",
        "🔒 Installing advanced protection modules...",
        "🛡️ Encrypting sensitive system files...",
        "🧠 Deploying AI-based defense algorithms...",
        "⚙️ Setting up real-time threat monitoring...",
        "📡 Securing network and communication ports...",
        "🧬 Activating adaptive firewall protocols...",
        "🛰️ Synchronizing with SEC global servers...",
        "🔄 Finalizing installation...",
        "✅ Security System is now Active!"
    ]

    for step in tqdm(range(len(steps)), desc="[🚀 Installing SEC Protection]", ascii=True, bar_format="{l_bar}{bar} [Elapsed: {elapsed}]"):
        print_colored(steps[step], "yellow")
        time.sleep(0.9)

    print_colored("\n✅ Installation complete. Your system is now fully protected!", "green")
    time.sleep(1)
    print_colored("🔥 You are now protected by SEC — Elite Cyber Defense 🔥", "cyan")
    print_colored("💀 Stealth & Power Mode Enabled 💀", "red")

    with open("security_log.txt", "a") as log:
        log.write(f"[SEC LOG] Protection activated on {time.ctime()}\n")

# Main Menu
def main_menu():
    print_logo()
    while True:
        print_colored("══════════ SEC MAIN MENU ══════════", "cyan")
        print_colored(" 1️⃣  Activate Phone Protection", "green")
        print_colored(" 2️⃣  Activate Windows Protection", "yellow")
        print_colored(" 3️⃣  Activate Linux Protection", "red")
        print_colored(" 4️⃣  Run Security Scan", "blue")
        print_colored(" 5️⃣  System Cleanup", "magenta")
        print_colored(" 6️⃣  Stealth Hacker Mode", "light_red")
        print_colored(" 0️⃣  Exit", "white")
        print_colored("═══════════════════════════════════", "cyan")

        choice = input(colored("\nSelect an option ➤ ", "light_cyan"))

        if choice == "1":
            print_colored("\n🔐 Activating PHONE Protection...", "green")
            fake_installation()
        elif choice == "2":
            print_colored("\n🛡️ Activating WINDOWS Protection...", "yellow")
            fake_installation()
        elif choice == "3":
            print_colored("\n🧰 Activating LINUX Protection...", "red")
            fake_installation()
        elif choice == "4":
            print_colored("\n🔍 Starting Full Security Scan...", "blue")
            fake_installation()
        elif choice == "5":
            print_colored("\n🧹 Running System Cleanup Utility...", "magenta")
            fake_installation()
        elif choice == "6":
            print_colored("\n💀 Activating Stealth Mode — You are now invisible!", "light_red")
            fake_installation()
        elif choice == "0":
            print_colored("\n👋 Exiting... Stay safe and protected!", "red")
            print_colored("🔐 Developed by SEC Company — The Future of Cyber Defense 🔐", "cyan")
            sys.exit()
        else:
            print_colored("❌ Invalid selection! Please choose a valid option.", "red")

# Start the program
if __name__ == "__main__":
    main_menu()
