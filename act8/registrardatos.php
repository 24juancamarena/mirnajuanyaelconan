<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Datos Recibidos</title>
</head>
<body>
  <p>Juan Carlos Camarena Pillado</p>
  <h2>Datos recibidos en el servidor</h2>
  <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
      echo "<ul>";
      foreach ($_POST as $campo => $valor) {
        echo "<li><strong>" . htmlspecialchars($campo) . ":</strong> " . htmlspecialchars($valor) . "</li>";
      }
      echo "</ul>";
    } else {
      echo "<p>No se recibieron datos por el m&eacute;todo POST.</p>";
    }
  ?>
  <p><a href="javascript:history.back()">Regresar al formulario</a></p>
</body>
</html>
