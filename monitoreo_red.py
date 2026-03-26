from netmiko import ConnectHandler
from tabulate import tabulate  # Instalación: pip install tabulate
import os

# --- CONFIGURACIÓN DE ACCESO ---
USUARIO = 'admin'
CLAVE = 'password123'

def monitorear_equipo(ip):
    dispositivo = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': USUARIO,
        'password': CLAVE,
    }

    try:
        print(f"\n🔍 Conectando para monitoreo: {ip}...")
        net_connect = ConnectHandler(**dispositivo)
        
        # Extraemos datos estructurados con TextFSM
        interfaces = net_connect.send_command("show ip interface brief", use_textfsm=True)
        net_connect.disconnect()

        # Lista para almacenar solo las que tienen problemas
        alertas = []

        for intf in interfaces:
            # Lógica de Inteligencia: Detectar fallos o desajustes
            status = intf['status'].lower()
            protocol = intf['protocol'].lower()

            if "down" in status or "down" in protocol:
                alertas.append([
                    intf['interface'], 
                    intf['ip_address'], 
                    intf['status'], 
                    intf['protocol']
                ])

        # Reporte Final
        if alertas:
            print(f"\n⚠️  ¡ALERTAS DETECTADAS EN {ip}!")
            print(tabulate(alertas, headers=["Interfaz", "IP", "Status", "Protocol"], tablefmt="grid"))
        else:
            print(f"✅ {ip}: Todas las interfaces operando normalmente.")

    except Exception as e:
        print(f"❌ Error al monitorear {ip}: {e}")

if __name__ == "__main__":
    # Leemos nuestro inventario de siempre
    if os.path.exists("dispositivos.txt"):
        with open("dispositivos.txt", "r") as f:
            ips = [linea.strip() for linea in f if linea.strip()]
        
        for ip in ips:
            monitorear_equipo(ip)
    else:
        print("❌ Archivo dispositivos.txt no encontrado.")