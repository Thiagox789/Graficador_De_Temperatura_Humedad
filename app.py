from flask import Flask, render_template, jsonify, send_from_directory
import json
import os
import sqlite3

app = Flask(__name__)

# Ruta del archivo JSON donde se guardan los datos
data_file = 'datos.json'

# Conectar a la base de datos SQLite
def conectar_db():
    conn = sqlite3.connect('datos.db')
    return conn

# Ruta principal
@app.route('/')
def home():
    """Página principal que muestra la gráfica y los datos."""
    return render_template('index.html')

# Ruta para obtener los datos más recientes
@app.route('/get_data')
def get_data():
    """Ruta que devuelve los datos de temperatura y humedad en formato JSON."""
    temperatura = None
    humedad = None
    fecha = None

    # Leer los datos desde el archivo JSON
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            try:
                stored_data = json.load(file)
                temperatura = stored_data.get("temperatura")
                humedad = stored_data.get("humedad")
                fecha = stored_data.get("fecha")
            except json.JSONDecodeError:
                print("Error al leer el archivo JSON")

    return jsonify({'temperatura': temperatura, 'humedad': humedad, 'fecha': fecha})

# Ruta para mostrar los registros desde la base de datos, ordenados de la fecha más reciente a la más antigua
@app.route('/ver_registros')
def ver_registros():
    """Ruta que muestra todos los registros de la base de datos ordenados por fecha más reciente."""
    conn = conectar_db()
    cursor = conn.cursor()

    # Obtener todos los registros de la tabla, ordenados por fecha descendente
    cursor.execute("SELECT * FROM registros ORDER BY fecha DESC")
    registros = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    conn.close()

    # Renderizar la plantilla para mostrar los registros
    return render_template('registros.html', registros=registros)

# Ruta para servir archivos estáticos (sonidos, imágenes, etc.)
@app.route('/static/sonidos/<path:filename>')
def sonidos(filename):
    """Sirve los archivos de sonido desde la carpeta static/sonidos."""
    return send_from_directory('static/sonidos', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
