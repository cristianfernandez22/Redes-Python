from netmiko import ConnectHandler
import os

# 1. CREDENCIALES
USUARIO = 'admin'
CLAVE = 'password123'

def cargar_config_desde_archivo(nombre_archivo):
    """Lee el archivo de configuración y devuelve una lista de líneas."""
    if not os.path.exists(nombre_archivo):
        print(f"❌ Error: El archivo {nombre_archivo} no existe.")
        return []
    
    with open(nombre_archivo, "r") as f:
        # Leemos el archivo y quitamos saltos de línea vacíos
        config = [linea.strip() for linea in f if linea.strip()]
    return config

def ejecutar_despliegue():
    # 2. CARGAMOS LOS COMANDOS DEL BACKUP
    comandos = cargar_config_desde_archivo("config_backup.txt")
    if not comandos: return

    # 3. LEEMOS LAS IPs
    if not os.path.exists("dispositivos.txt"):
        print("❌ Error: No existe dispositivos.txt")
        return

    with open("dispositivos.txt", "r") as f:
        ips = [l.strip() for l in f if l.strip()]

    for ip in ips:
        equipo = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': USUARIO,
            'password': CLAVE,
        }

        print(f"\n📂 Cargando configuración de backup en: {ip}...")

        try:
            net_connect = ConnectHandler(**equipo)
            
            # Enviamos el archivo completo como un set de configuración
            output = net_connect.send_config_set(comandos)
            
            print(f"✅ Backup aplicado con éxito en {ip}")
            print("-" * 30)
            print(output)
            print("-" * 30)
            
            net_connect.disconnect()

        except Exception as e:
            print(f"⚠️ Error al conectar con {ip}: {e}")

if __name__ == "__main__":
    ejecutar_despliegue()