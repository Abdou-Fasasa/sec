import time
import sys
import random
import subprocess
from colorama import Fore, Style, init

# Initialize colorama for Windows
init(autoreset=True)

def install_requirements():
    print_colored("\n[✔] Installing required libraries...", Fore.YELLOW)
    subprocess.run(["pip", "install", "colorama"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print_colored("[✔] All dependencies installed!", Fore.GREEN)

def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

def fake_installation():
    loading_messages = [
        "Downloading security modules...",
        "Installing protection components...",
        "Verifying installation...",
        "Finalizing setup..."
    ]
    
    for _ in range(10):
        print_colored(random.choice(loading_messages), Fore.YELLOW)
        time.sleep(1)
    
    print_colored("\n[✔] Protection installed successfully!", Fore.GREEN)

def main_menu():
    install_requirements()
    while True:
        print_colored("\n\t📌 Security Activation Tool 📌", Fore.CYAN)
        print_colored("\n1️⃣ Activate protection for phone", Fore.BLUE)
        print_colored("2️⃣ Activate protection for Windows", Fore.BLUE)
        print_colored("3️⃣ Activate protection for Linux", Fore.BLUE)
        print_colored("0️⃣ Exit", Fore.RED)
        
        choice = input(Fore.MAGENTA + "\nChoose an option: " + Style.RESET_ALL)
        
        if choice == "1":
            print_colored("\n🔒 Activating protection for phone...", Fore.YELLOW)
            fake_installation()
        elif choice == "2":
            print_colored("\n🔒 Activating protection for Windows...", Fore.YELLOW)
            fake_installation()
        elif choice == "3":
            print_colored("\n🔒 Activating protection for Linux...", Fore.YELLOW)
            fake_installation()
        elif choice == "0":
            print_colored("\n👋 Goodbye!", Fore.RED)
            sys.exit()
        else:
            print_colored("❌ Invalid choice, try again!", Fore.RED)

if __name__ == "__main__":
    main_menu()
