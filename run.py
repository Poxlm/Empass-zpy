import subprocess
import os
from colorama import Fore

def run_flask(port):
    os.environ["FLASK_APP"] = "app.py" 
    os.environ["FLASK_ENV"] = "development"
    subprocess.Popen(["flask", "run", "-p", str(port)])

def run_serveo(port, subdomain):
    subprocess.Popen(["ssh", "-R", f"{subdomain}:80:localhost:{port}", "serveo.net"])

def print_menu():
    print_colored_text("╔════════════════════════════════╗", Fore.CYAN)
    print_colored_text("║  🌐 PoxlM DTool - EmpassZpy 🚀  ║", Fore.CYAN)
    print_colored_text("╚════════════════════════════════╝", Fore.CYAN)
    print("1 - Run Flask Server")
    print("2 - Run Serveo with Flask Server")
    print("3 - Exit")

def print_colored_text(text, color):
    print(f"{color}{text}")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ")
        try:
            choice = int(choice)
            if choice == 1:
                port = input("Enter the port to run the Flask server on: ")
                run_flask(port)
            elif choice == 2:
                port = input("Enter the port to run the Flask server on: ")
                subdomain = input("Enter the subdomain for Serveo: ")
                run_flask(port)
                run_serveo(port, subdomain)
            elif choice == 3:
                print("Goodbye! 👋")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
