import os
import platform

# Lista de nodos para probar (puedes poner IPs de tu red local si quieres)
nodos = ["8.8.8.8", "1.1.1.1", "google.com"]

def test_red():
    print(f"--- Iniciando chequeo en: {platform.system()} ---")
    
    for host in nodos:
        # Lógica de redes: Windows usa '-n', Linux usa '-c'
        param = "-n" if platform.system().lower() == "windows" else "-c"
        comando = f"ping {param} 1 {host}"
        
        # Ejecutamos el comando de consola desde Python
        respuesta = os.system(comando)
        
        if respuesta == 0:
            print(f"✅ {host} responde correctamente.")
        else:
            print(f"❌ {host} NO responde.")

if __name__ == "__main__":
    test_red()