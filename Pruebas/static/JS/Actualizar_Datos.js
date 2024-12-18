let alertaReproducida = false;

// Función para obtener los datos de temperatura, humedad y fecha desde Flask
async function obtenerDatos() {
    try {
        const response = await fetch('/get_data');
        const data = await response.json();

        document.getElementById('temperatura').textContent = data.temperatura || 'Cargando...';
        document.getElementById('humedad').textContent = data.humedad || 'Cargando...';
        document.getElementById('fecha').textContent = data.fecha || 'Cargando...';

        if (data.temperatura >= 30 && !alertaReproducida) {
            const audio = new Audio('/static/sonidos/alerta.mp3');
            await audio.play();
            alertaReproducida = true;
        } else if (data.temperatura < 30) {
            alertaReproducida = false;
        }
    } catch (error) {
        console.error("Error al obtener los datos:", error);
    }
}

// Actualizar la gráfica y los datos cada 1 segundo
setInterval(function () {
    // Actualizar la imagen de la gráfica
    document.getElementById('grafica').src = '/static/grafica.png?' + new Date().getTime();
    
    // Obtener los nuevos datos de temperatura, humedad y fecha
    obtenerDatos();
}, 1000); // Actualiza cada 1 segundo
