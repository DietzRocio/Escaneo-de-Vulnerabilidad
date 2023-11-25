# vulnerabilities/weak_passwords.py

import re

def check_weak_password(password):
    # Verificar la longitud mínima de la contraseña
    if len(password) < 8:
        return True

    # Verificar complejidad (por ejemplo, al menos una letra y un número)
    if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
        return True

    return False
