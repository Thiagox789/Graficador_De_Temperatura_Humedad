import json
import sqlite3
import time
import os

def conectar_db():
    conn = sqlite3.connect('datos.db')
    return conn

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


def subir_a_bd():
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)

        if datos:
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO registros (temperatura, humedad, fecha) VALUES (?, ?, ?)",
                           (datos['temperatura'], datos['humedad'], datos['fecha']))

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
    print("Subiendo datos a la base de datos")
    while True:
        subir_a_bd()
        time.sleep(60)
