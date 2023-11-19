# Escaneo-de-Vulnerabilidad
Diseñado para identificar posibles puntos débiles en la seguridad de un sistema. 
Utiliza módulos de detección de contraseñas débiles y puertos abiertos para proporcionar una visión general de la postura de seguridad de un host.

Funcionalidades Principales
- Detección de contraseñas débiles mediante reglas de complejidad y longitud.
- Detección de puertos abiertos en un host especificado.
- Generación de informes de texto para resumir los resultados del escaneo.

Para escanear un host, utiliza el siguiente comando: python main.py --passwords --ports 'host_a_escanear'
