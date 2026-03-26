# Network Programmability & Automation Suite (Python)

Este repositorio contiene una colección de herramientas desarrolladas en **Python** para la automatización de tareas operativas en entornos de red multimarca (Cisco, Juniper, etc.). El proyecto demuestra la transición de la gestión tradicional por CLI hacia infraestructuras programables.

## 🚀 Funcionalidades Principales

La suite se divide en módulos especializados para el ciclo de vida de la red:

* **Gestión de Conectividad:** Scripts de automatización mediante SSH para ejecución de comandos masivos (`conexion_ssh.py`).
* **Respaldo y Recuperación:** Automatización de backups de configuración para dispositivos críticos (`respaldo_router_cisco.py`).
* **Monitoreo & Diagnóstico:** Herramientas de análisis de estado y salud de la red en tiempo real (`monitoreo_red.py`, `diagnostico_red.py`).
* **Gestión de Inventarios:** Control de dispositivos mediante archivos de datos externos (`dispositivos.txt`).

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Librerías clave:** Netmiko / Paramiko (SSH), OS, Time.
* **Formatos de Datos:** TXT / LOG para reportes y respaldos.

## 📦 Estructura del Proyecto
* `conexion_ssh.py`: Motor base para sesiones remotas.
* `respaldo_router_cisco.py`: Script para extracción de `running-config`.
* `diagnostico_red.py`: Validación de tablas de ruteo y estados de interfaces.
* `reporte_red.txt`: Output generado automáticamente con el estado del inventario.

## 🔧 Uso
1. Definir la lista de IPs y credenciales en `dispositivos.txt`.
2. Ejecutar el script de monitoreo o respaldo según la necesidad:
   ```bash
   python3 monitoreo_red.py
