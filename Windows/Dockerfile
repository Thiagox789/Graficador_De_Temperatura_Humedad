# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias del archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto 5000 (el puerto en el que Flask correrá por defecto)
EXPOSE 5000

# Ejecuta los scripts en segundo plano para que no se bloqueen entre sí
CMD python procesar_datos.py & python app.py & python DB.py && tail -f /dev/null
