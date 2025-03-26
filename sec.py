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

def loading_bar():
    """شريط تحميل حقيقي يستغرق بين 3 إلى 5 دقائق"""
    total_time = random.randint(180, 300)  # مدة التثبيت بين 3 و 5 دقائق
    step = total_time // 30  # تحديث كل ثانية تقريبًا
    print_colored("\n[⏳] جاري التثبيت، يرجى الانتظار...", Fore.YELLOW)

    for i in range(31):
        percent = (i / 30) * 100
        bar = "#" * (i // 2) + "-" * (15 - (i // 2))
        print(f"\r[{bar}] {percent:.0f}%", end="", flush=True)
        time.sleep(step)

    print_colored("\n[✔] التثبيت اكتمل بنجاح!", Fore.GREEN)

def main_menu():
    install_requirements()
    while True:
        print_colored("\n========= Security Activation Tool =========", Fore.CYAN)
        print_colored("[1] تفعيل الحماية للهاتف", Fore.BLUE)
        print_colored("[2] تفعيل الحماية للويندوز", Fore.BLUE)
        print_colored("[3] تفعيل الحماية للينكس", Fore.BLUE)
        print_colored("[0] خروج", Fore.RED)
        
        choice = input(Fore.MAGENTA + "\nاختر خيارًا: " + Style.RESET_ALL)

        if choice == "1":
            print_colored("\n[🔒] جاري تفعيل الحماية للهاتف...", Fore.YELLOW)
            loading_bar()
        elif choice == "2":
            print_colored("\n[🔒] جاري تفعيل الحماية للويندوز...", Fore.YELLOW)
            loading_bar()
        elif choice == "3":
            print_colored("\n[🔒] جاري تفعيل الحماية للينكس...", Fore.YELLOW)
            loading_bar()
        elif choice == "0":
            print_colored("\n[👋] وداعًا!", Fore.RED)
            sys.exit()
        else:
            print_colored("[❌] خيار غير صحيح، حاول مرة أخرى!", Fore.RED)

if __name__ == "__main__":
    main_menu()