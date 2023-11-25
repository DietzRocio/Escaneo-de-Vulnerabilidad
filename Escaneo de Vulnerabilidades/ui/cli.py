# ui/cli.py

import argparse
from Vulnerabilities import weak_passwords, open_ports

def parse_args():
    parser = argparse.ArgumentParser(description="Simple Vulnerability Scanner")
    parser.add_argument("target", help="Target host to scan")
    parser.add_argument("--passwords", action="store_true", help="Check for weak passwords")
    parser.add_argument("--ports", action="store_true", help="Check for open ports")

    return parser.parse_args()

def main():
    args = parse_args()

    if args.passwords:
        password = input("Enter a password to check: ")
        if weak_passwords.check_weak_password(password):
            print("Weak password detected!")
        else:
            print("Password is strong.")

    if args.ports:
        target_host = args.target
        target_ports = [80, 443, 22]  # You can customize the list of ports to scan
        open_ports_list = open_ports.check_open_ports(target_host, target_ports)

        if open_ports_list:
            print("Open ports detected:")
            for port, service in open_ports_list:
                print(f"Port {port}: {service}")
        else:
            print("No open ports detected.")

if __name__ == "__main__":
    main()
