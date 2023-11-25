# vulnerabilities/open_ports.py

import socket

def check_open_ports(host, ports):
    # Implementa la lógica para verificar si los puertos dados están abiertos en el host
    # Utiliza la biblioteca `socket` de Python para realizar conexiones
    # Retorna una lista de puertos abiertos junto con el servicio que está escuchando en cada puerto

    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((host, port))
                service = socket.getservbyport(port)
                open_ports.append((port, service))
        except (socket.timeout, socket.error, OSError):
            pass
    return open_ports
