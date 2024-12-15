#!/bin/bash

# Función para manejar la interrupción con Ctrl+C
trap 'echo "Interrumpido por el usuario. Deteniendo procesos..."; pkill python; pkill python3; exit 1' SIGINT

# Matar todos los procesos de Python (python y python3)
echo "Matar todos los procesos de Python..."
pkill python
pkill python3

# Esperar unos segundos para asegurarse de que los procesos se hayan detenido
sleep 2

# Cambia al directorio del proyecto
cd /root/Graficador_De_Temperatura_Humedad || exit
# Verificar que no haya procesos de python en ejecución
echo "Verificando procesos restantes de Python..."
ps aux | grep python

# Ejecutar los archivos de Python en el orden adecuado
echo "Ejecutando app.py..."
python3 /root/Graficador_De_Temperatura_Humedad/app.py &

# Esperar un poco para asegurarse de que `app.py` se haya iniciado
sleep 2

echo "Ejecutando procesar_datos.py..."
python3 /root/Graficador_De_Temperatura_Humedad/procesar_datos.py &

# Esperar un poco para asegurarse de que `procesar_datos.py` se haya iniciado
sleep 2

echo "Ejecutando DB.py..."
python3 /root/Graficador_De_Temperatura_Humedad/DB.py &

# Esperar a que los procesos en segundo plano terminen (sin bloquear)
wait

echo "Todos los procesos han sido iniciados o interrumpidos."
