import os
import platform
from datetime import datetime

def realizar_ping(objetivo):
    # Comando silencioso
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = f"ping {parametro} 1 {objetivo} > nul 2>&1"
    
    status = os.system(comando)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Estos emojis son los que causan el error si no usamos utf-8
    if status == 0:
        resultado = f"[{ahora}] ✅ {objetivo.ljust(15)} | ALCANZABLE"
    else:
        resultado = f"[{ahora}] ❌ {objetivo.ljust(15)} | SIN RESPUESTA"
    
    print(resultado)
    return resultado

def main():
    print("=== INICIANDO ESCANEO Y GENERANDO REPORTE ===")
    
    try:
        # AÑADIMOS encoding="utf-8" AQUÍ 👇
        with open("dispositivos.txt", "r", encoding="utf-8") as archivo_ips:
            # Y TAMBIÉN AQUÍ 👇
            with open("reporte_red.txt", "a", encoding="utf-8") as reporte:
                reporte.write(f"\n--- Sesión de escaneo: {datetime.now()} ---\n")
                
                for linea in archivo_ips:
                    ip = linea.strip()
                    if ip:
                        resultado_linea = realizar_ping(ip)
                        reporte.write(resultado_linea + "\n")
        
        print("\n✅ Escaneo completado. Revisa 'reporte_red.txt'.")
                    
    except FileNotFoundError:
        
        print("Error: No encontré 'dispositivos.txt'.")

if __name__ == "__main__":
    main()