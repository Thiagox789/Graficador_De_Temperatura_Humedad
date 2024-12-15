#!/bin/bash

trap 'echo "Interrumpido por el usuario. Deteniendo procesos..."; pkill python; pkill python3; exit 1' SIGINT
)
echo "Matar todos los procesos de Python..."
pkill python
pkill python3

sleep 2
cd /root/Graficador_De_Temperatura_Humedad || exit
echo "Verificando procesos restantes de Python..."
ps aux | grep python

echo "Ejecutando app.py..."
python3 /root/Graficador_De_Temperatura_Humedad/app.py &
sleep 2

echo "Ejecutando procesar_datos.py..."
python3 /root/Graficador_De_Temperatura_Humedad/procesar_datos.py &
sleep 2

echo "Ejecutando DB.py..."
python3 /root/Graficador_De_Temperatura_Humedad/DB.py &

wait
echo "Todos los procesos han sido iniciados o interrumpidos."
