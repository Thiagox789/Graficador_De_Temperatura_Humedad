import sqlite3
import plotly.graph_objects as go
from datetime import datetime

def obtener_datos():
    """Obtiene los datos de temperatura y humedad de la base de datos."""
    try:
        conn = sqlite3.connect('datos.db')
        cursor = conn.cursor()

        cursor.execute("SELECT fecha, temperatura, humedad FROM registros")
        datos = cursor.fetchall()

        conn.close()
        return datos
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return []

def graficar_temperatura_humedad():
    """Genera un gráfico de temperatura y humedad interactivo."""
    datos = obtener_datos()

    if not datos:
        print("No se encontraron datos para graficar.")
        return

    # Extraer datos
    fechas = [datetime.strptime(fila[0], '%Y-%m-%d %H:%M:%S') for fila in datos]  # Ajustar el formato según sea necesario
    temperaturas = [fila[1] for fila in datos]
    humedades = [fila[2] for fila in datos]

    # Crear gráfico interactivo con Plotly
    fig = go.Figure()

    # Añadir traza para temperatura
    fig.add_trace(go.Scatter(x=fechas, y=temperaturas, mode='lines+markers', name='Temperatura (°C)', marker=dict(symbol='triangle-up')))

    # Añadir traza para humedad
    fig.add_trace(go.Scatter(x=fechas, y=humedades, mode='lines+markers', name='Humedad (%)', marker=dict(symbol='circle')))

    # Configuración del gráfico
    fig.update_layout(
        title="Temperatura y Humedad",
        xaxis_title="Fecha y Hora",
        yaxis_title="Valores",
        xaxis=dict(tickformat='%Y-%m-%d %H:%M:%S'),  # Formato de fecha
        autosize=True,
        hovermode="closest",
        xaxis_rangeslider_visible=True  # Habilitar el control deslizante para el zoom
    )

    # Mostrar gráfico
    fig.show()

if __name__ == "__main__":
    graficar_temperatura_humedad()
