# main.py

from ui import cli
from reporting import text_report
from Vulnerabilities import weak_passwords, open_ports

def main():
    args = cli.parse_args()

    weak_password_result = None
    open_ports_result = None

    if args.passwords:
        password = input("Enter a password to check: ")
        weak_password_result = weak_passwords.check_weak_password(password)
        if weak_password_result:
            print("Weak password detected!")
        else:
            print("Password is strong.")

    if args.ports:
        target_host = args.target
        target_ports = [80, 613, 22]  
        open_ports_result = open_ports.check_open_ports(target_host, target_ports) 

        if open_ports_result:
            print("Open ports detected:")
            for port, service in open_ports_result:
                print(f"Port {port}: {service}")
        else:
            print("No open ports detected.")

    # Genera y muestra informe 
    report = text_report.generate_text_report(weak_password_result, open_ports_result)
    print("\n--- Scan Report ---\n")
    print(report)

if __name__ == "__main__":
    main()
