import subprocess
import sys
import time
import random

# قائمة المكتبات المطلوبة
REQUIRED_LIBRARIES = ["colorama"]

def install_requirements():
    """تثبيت المكتبات المطلوبة تلقائيًا إذا لم تكن مثبتة."""
    for lib in REQUIRED_LIBRARIES:
        try:
            __import__(lib)
        except ModuleNotFoundError:
            print(f"\n[!] {lib} غير مثبت. جاري التثبيت...")
            subprocess.run([sys.executable, "-m", "pip", "install", lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[✔] {lib} تم تثبيته بنجاح!\n")
            # إعادة تحميل المكتبة بعد التثبيت
            globals()[lib] = __import__(lib)

# تثبيت المكتبات المطلوبة أولًا
install_requirements()

# استيراد المكتبات بعد التثبيت
from colorama import Fore, Style, init

# تهيئة colorama
init(autoreset=True)

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