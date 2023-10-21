import subprocess
import os

def run_flask(port):
    os.environ["FLASK_APP"] = "app.py" 
    os.environ["FLASK_ENV"] = "development"
    subprocess.Popen(["flask", "run", "-p", str(port)])

def run_serveo(port, subdomain):
    subprocess.Popen(["ssh", "-R", f"{subdomain}:80:localhost:{port}", "serveo.net"])

def main():
    port = input("Enter the port to run the Flask server on: ")
    subdomain = input("Enter the subdomain for Serveo: ")
    run_flask(port)
    run_serveo(port, subdomain)

if __name__ == "__main__":
    main()