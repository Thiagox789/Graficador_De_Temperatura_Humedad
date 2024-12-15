from flask import Flask, render_template, jsonify, send_from_directory, url_for
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
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    temperatura = None
    humedad = None
    fecha = None
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

@app.route('/Registros')
def ver_registros():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros ORDER BY fecha DESC")
    registros = cursor.fetchall()
    conn.close()
    return render_template('registros.html', registros=registros)

@app.route('/dashboard')
def dashboard():
    return render_template('pagina1.html')

@app.route('/graficos')
def graficos():
    return render_template('Graficos.html')

@app.route('/salir')
def salir():
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
