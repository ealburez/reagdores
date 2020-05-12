<html>
<head>
  <title>getElementById example</title>
</head>
<body>
  <?php
    echo "Hello World!";
  ?>
  <label for "button1">Regador1 </label><button onclick="changeColor('yellow');" id="button1">Probar</button><br> 
  <p id="tiempo2"> 00:00 </p>
  
  <label for "estado1"> Activar regador</label><input type="checkbox" id="estado1" name="estado1" checked><br>
  
  <label for="hora1">Hora de inicio</label><input type="time" id="hora1" value="12:00" name="hora1"> <br>
  
  <label for="tiempo1">Tiempo (en minutos):</label><input type="number" id="tiempo1" name="tiempo1" value="10" min="1" max="100"><br>
  
  <p id="text1">Regadores</p>
  <p id="fecha0">Date/Time:</p>
  <button onclick="changeColor('yellow');">azul</button>
  <button onclick="changeColor('red');">red</button> <br> <br>
  <button onclick="updateDate();">Fecha</button> <br> <br>
  
</body>
</html>
