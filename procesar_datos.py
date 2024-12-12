import serial
import time
import matplotlib.pyplot as plt
from datetime import datetime

# Configuración del puerto serie
arduino = serial.Serial('COM3', 9600, timeout=1)  # Cambia 'COM3' por el puerto correcto

# Inicializar listas para almacenar datos
temperaturas = []
humedades = []
tiempos = []

def graficar_datos():
    """Genera una gráfica con los datos almacenados y la guarda como PNG."""
    plt.figure(figsize=(10, 5))
    plt.plot(tiempos, temperaturas, label="Temperatura (°C)", color="red", marker="o")
    plt.plot(tiempos, humedades, label="Humedad (%)", color="blue", marker="o")
    plt.xlabel("Tiempo")
    plt.ylabel("Valores")
    plt.legend()
    plt.title("Temperatura y Humedad")
    plt.grid(True)
    plt.savefig("static/grafica.png")
    plt.close()

print("Leyendo datos del Arduino... Presiona Ctrl+C para detener.")

try:
    while True:
        if arduino.in_waiting > 0:
            # Leer datos del puerto serie
            linea = arduino.readline().decode('utf-8').strip()
            print(f"Datos recibidos: {linea}")
            
            # Procesar los datos (Temperatura: xx °C, Humedad: xx %)
            if "Temperatura" in linea and "Humedad" in linea:
                partes = linea.split(", ")
                temperatura = float(partes[0].split(": ")[1].split(" ")[0])
                humedad = float(partes[1].split(": ")[1].split(" ")[0])
                
                # Agregar datos a las listas
                temperaturas.append(temperatura)
                humedades.append(humedad)
                tiempos.append(datetime.now().strftime("%H:%M:%S"))
                
                # Limitar los datos a las últimas 10 muestras
                if len(temperaturas) > 10:
                    temperaturas.pop(0)
                    humedades.pop(0)
                    tiempos.pop(0)
                
                # Generar la gráfica
                graficar_datos()
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa detenido.")
finally:
    arduino.close()
