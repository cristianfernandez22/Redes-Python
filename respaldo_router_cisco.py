from netmiko import ConnectHandler
import datetime
import os

# --- 1. DATOS DE ACCESO (Ajusta según tu red) ---
USUARIO = 'admin'
CLAVE = 'password123'
SECRET = 'admin'  # Contraseña de enable
CARPETA_LOCAL = 'Respaldos_Cisco'

def guardar_archivo(nombre_equipo, contenido):
    """Función para escribir el archivo en el disco."""
    # Nombre con fecha: RouterCore_2026-03-21.txt
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d")
    archivo_final = f"{nombre_equipo}_{fecha_hoy}.txt"
    ruta = os.path.join(CARPETA_LOCAL, archivo_final)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"💾 Archivo guardado: {ruta}")

def realizar_respaldo(ip):
    """Función para conectar y extraer la configuración."""
    router_cisco = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': USUARIO,
        'password': CLAVE,
        'secret': SECRET,
    }

    try:
        print(f"\n🔗 Conectando al Router Cisco: {ip}...")
        net_connect = ConnectHandler(**router_cisco)
        
        # Entrar en modo enable y quitar pausas de lectura
        net_connect.enable()
        net_connect.send_command("terminal length 0")

        # Obtener el Hostname real del equipo
        prompt = net_connect.find_prompt()
        hostname = prompt.replace('#', '').replace('>', '')

        print(f"📥 Extrayendo Running-Config de {hostname}...")
        configuracion = net_connect.send_command("show running-config")

        # Guardar el resultado en la carpeta
        guardar_archivo(hostname, configuracion)

        net_connect.disconnect()
        print(f"✅ Respaldo de {hostname} completado.")

    except Exception as e:
        print(f"❌ Falló el respaldo en {ip}: {e}")

def iniciar():
    """Función principal que orquestra todo."""
    # A. Verificar si existe el archivo de IPs
    if not os.path.exists("dispositivos.txt"):
        print("❌ Error: No se encuentra 'dispositivos.txt'")
        return

    # B. CREAR LA CARPETA SI NO EXISTE (Ahora se hace al inicio)
    if not os.path.exists(CARPETA_LOCAL):
        os.makedirs(CARPETA_LOCAL)
        print(f"📁 Carpeta '{CARPETA_LOCAL}' creada en: {os.getcwd()}")

    # C. Leer las IPs
    with open("dispositivos.txt", "r") as f:
        ips = [linea.strip() for linea in f if linea.strip()]

    print(f"🚀 Iniciando proceso de backup para {len(ips)} equipos.")
    
    # D. Recorrer la lista
    for ip in ips:
        realizar_respaldo(ip)

if __name__ == "__main__":
    iniciar()