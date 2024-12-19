import serial
import time
import json
from datetime import datetime


# Configuración del puerto serie
arduino = serial.Serial('COM3', 9600, timeout=1)  # Cambia 'COM3' por el puerto correcto

# Inicializar listas para almacenar datos
temperaturas = []
humedades = []
tiempos = []


def guardar_datos_json(temperatura, humedad):
    """Guarda los datos de temperatura y humedad en un archivo JSON."""
    datos = {'temperatura': temperatura, 'humedad': humedad, 'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    # Guardar datos en archivo JSON
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo)
    print(f"Datos guardados en JSON: {datos}")

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

                guardar_datos_json(temperatura, humedad)

                temperaturas.append(temperatura)
                humedades.append(humedad)
                tiempos.append(datetime.now().strftime("%H:%M:%S"))
                
                # Limitar los datos a las últimas 10 muestras
                if len(temperaturas) > 10:
                    temperaturas.pop(0)
                    humedades.pop(0)
                    tiempos.pop(0)
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa detenido.")
finally:
    arduino.close()
