<html>
<head>
  <title>Control de regadores</title>
</head>
<body>
	<p id="text1">Regadores</p>

	<?php  
  	$numRega=3;
	
	echo "<label>Total regadores:</label><label id='numRega'> $numRega</label><br><br>";	
	for ($i = 1; $i <= $numRega; $i++) {
			if ($i%2 == 1){
				$checa="checked";
			}else {
				$checa="";
			}
		
  		/*Creación de los controles de los regadores*/
			echo "<label for='button_$i'>Regador $i </label><button onclick='changeColor('yellow');' id='button_$i'>'Encender 5 minutos'</button><br>";
			echo "<label for='estado_$i'> Habilitar</label><input type='checkbox' id='estado_$i' name='estado_$i' $checa><br>";
			echo "<label for='hora_$i'>Hora de inicio</label><input type='time' id='hora_$i' value='12:00' name='hora_$i'> <br>";
			echo "<label for='tiempo_$i'>Tiempo (en minutos):</label><input type='number' id='tiempo_$i' name='tiempo_$i' value='10' min='1' max='100'><br>";
	}
	?>
	
	<button onclick="updateDate();" id="prog1">Programar</button> <br>
	<p id="confirm1">No guardado</p><br>
  
	<p id="text1">Regadores</p>
  <p id="fecha0">Date/Time:</p>
  <button onclick="changeColor('yellow');">azul</button>
  <button onclick="changeColor('red');">red</button> <br> <br>
  <button onclick="updateDate();">Fecha</button> <br> <br>
  
</body>
</html>
