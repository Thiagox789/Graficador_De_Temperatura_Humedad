import json
import sqlite3
import time
import os

# Función para conectar a la base de datos SQLite
def conectar_db():
    conn = sqlite3.connect('datos.db')
    return conn

# Función para crear la tabla en la base de datos si no existe
def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperatura REAL,
            humedad REAL,
            fecha TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Función para subir datos a la base de datos
def subir_a_bd():
    # Leer los datos desde el archivo JSON
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as archivo:
            # Leer el archivo y convertirlo a un diccionario de Python
            datos = json.load(archivo)

        if datos:
            # Conectar a la base de datos
            conn = conectar_db()
            cursor = conn.cursor()

            # Subir el único registro de datos a la base de datos
            cursor.execute("INSERT INTO registros (temperatura, humedad, fecha) VALUES (?, ?, ?)",
                           (datos['temperatura'], datos['humedad'], datos['fecha']))

            # Confirmar los cambios y cerrar la conexión
            conn.commit()
            conn.close()

            print("Datos subidos a la base de datos.")
        else:
            print("No hay datos para subir.")
    else:
        print("El archivo JSON no existe.")

if __name__ == "__main__":
    # Crear la tabla si no existe
    crear_tabla()

    print("Subiendo datos a la base de datos. Presiona Ctrl+C para detener.")

    # Subir los datos constantemente cada 60 segundos sin borrar el archivo JSON
    while True:
        subir_a_bd()
        # Esperar 60 segundos antes de volver a intentar
        time.sleep(60)
