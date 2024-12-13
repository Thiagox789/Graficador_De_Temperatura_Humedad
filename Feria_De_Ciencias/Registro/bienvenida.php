<?php
 session_start();
 if(!isset($_SESSION['usuario'])){
    echo'
    <script>
        alert("Por favor inicie sesion");
    </script>
    ';
    header("location: index.php");
    session_destroy();
    die();
    
 }
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cerrar sesión</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f8f8f8;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bienvenido a mi Página</h1>
        <a href="php/cerrar.php">Cerrar sesión</a>
        <p>Usted ya jugo</p>
        <p></p>
    </div>
</body>
</html>
