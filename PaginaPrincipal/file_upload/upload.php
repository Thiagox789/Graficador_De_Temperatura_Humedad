<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $targetDirectory = "uploads/"; // Directorio donde se guardarán los archivos cargados

    foreach ($_FILES["fileToUpload"]["tmp_name"] as $key => $tmp_name) {
        $targetFile = $targetDirectory . basename($_FILES["fileToUpload"]["name"][$key]);

        // Verificar si el archivo ya existe
        if (file_exists($targetFile)) {
            echo "El archivo ya existe.";
        } else {
            // Mover el archivo al directorio de destino
            if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"][$key], $targetFile)) {
                echo "El archivo " . basename($_FILES["fileToUpload"]["name"][$key]) . " ha sido cargado con éxito.";
            } else {
                echo "Hubo un error al cargar el archivo.";
            }
        }
    }
}
?>