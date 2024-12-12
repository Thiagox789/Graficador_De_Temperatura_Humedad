from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Ruta del archivo JSON donde se guardan los datos
data_file = 'datos.json'

@app.route('/')
def home():
    """Página principal que muestra la gráfica y los datos."""
    return render_template('index.html')

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
                # Asegurarse de que los datos existen en el archivo
                temperatura = stored_data.get("temperatura")
                humedad = stored_data.get("humedad")
                fecha = stored_data.get("fecha")
            except json.JSONDecodeError:
                print("Error al leer el archivo JSON")

    # Devolver los datos como un JSON
    return jsonify({'temperatura': temperatura, 'humedad': humedad, 'fecha': fecha})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
