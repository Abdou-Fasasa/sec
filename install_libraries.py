import subprocess
import sys
import time
import os
from termcolor import colored
import pyfiglet

# ==== List of Required Libraries ====
libraries = [
    "colorama",
    "tqdm",
    "pyfiglet",
    "termcolor"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    banner = pyfiglet.figlet_format("SEC PROTECTION", font="slant")
    print(colored(banner, "red"))
    print(colored("══════════════════════════════════════════════════════", "cyan"))
    print(colored("        🔐 Ultimate Python Security Setup 🔐", "yellow"))
    print(colored("══════════════════════════════════════════════════════\n", "cyan"))
    time.sleep(1)

def install_library(lib):
    try:
        __import__(lib)
        print(colored(f"[✔] {lib} is already installed.", "green"))
    except ImportError:
        print(colored(f"[+] Installing {lib}...", "yellow"))
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        print(colored(f"[✔] {lib} installed successfully!", "green"))
        time.sleep(0.5)

def install_all():
    print(colored("\n[⚙️] Starting secure installation process...\n", "blue"))
    for lib in libraries:
        install_library(lib)
    print(colored("\n[✔] All libraries are now installed and ready to use!\n", "cyan"))

def show_closing_message():
    print(colored("══════════════════════════════════════════════════════", "cyan"))
    thanks = pyfiglet.figlet_format("SEC", font="digital")
    print(colored(thanks, "light_red"))
    print(colored("       ✅ Setup completed successfully!", "green"))
    print(colored("       🔒 System is now protected and ready!", "cyan"))
    print(colored("══════════════════════════════════════════════════════", "cyan"))
    print(colored("       👨‍💻 Developed by SEC Company", "light_yellow"))
    print(colored("══════════════════════════════════════════════════════", "cyan"))

if __name__ == "__main__":
    print_banner()
    install_all()
    show_closing_message()
