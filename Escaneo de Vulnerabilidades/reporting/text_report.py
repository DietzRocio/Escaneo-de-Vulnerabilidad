# reporting/text_report.py

def generate_text_report(weak_password_result, open_ports_result):
    report = "Vulnerability Scan Report:\n"

    if weak_password_result:
        report += "\nWeak Passwords Detected:\n"
        report += f"Password: {weak_password_result}\n"

    if open_ports_result:
        report += "\nOpen Ports Detected:\n"
        for port, service in open_ports_result:
            report += f"Port {port}: {service}\n"

    return report
