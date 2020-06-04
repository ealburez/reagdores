<html>
<head>
  <title>Control de regadores</title>
</head>
<body>
	<p id="text1">Regadores Alburez</p>

	<?php  
  	//Variables
  	$numRega=-1; //numero de regadores
	$confDir="regadores.conf"; //archivo para leer - Path /var/www/html
	$confFile = fopen($confDir, "r") or die("Unable to open file!");
	$input=array();
    $color="yellow";
	
	//load data from file
	while(!feof($confFile)) {
  		$input[]=explode(",",fgets($confFile));
		$numRega+=1;
	}
    
	fclose($confFile);
    
	print_r($input);
	
    
    //Encabezado
    echo "<br><label>Total regadores:</label><label id='numRega'> $numRega</label><br><br>";	
	//Loop para crear los elementos
	for ($i = 0; $i < $numRega; $i++) {
			
        $checa="";
        if ($input[$i][1] == 1){
				$checa="checked";
        }
  		/*Creación de los controles de los regadores*/
		
       	//Crear nuevo espacio
  		echo "<div class='box_$i'> Regador $i"

        //checkbox Habilita
        echo "<br> <label for='estado_$i'>Regador $i </label> <input type='checkbox' id='estado_$i' name='estado_$i'$checa>";
        //checkbox Cada dos días
        echo "<label for='freq_$i'>Diario: </label><input type='checkbox' id='freq_$i' name='estado_$i' $checa>";
 		
        //Hora inicio
        echo "<label for='hora_$i'>Hora de inicio</label><input type='time' id='hora_$i' value=".$input[$i][2]." name='hora_$i'> <br>";
		//Duración	
        echo "<label for='tiempo_$i'>Tiempo (en minutos):</label><input type='number' id='tiempo_$i' name='tiempo_$i' value=".$input[$i][4]." min='1' max='100'><br><br>";
        echo "</div>"
	}
	?>
	<!--Programar la configuracion en RPI-->
	<button onclick="updateDate();" id="prog1">Programar</button> <br>
	<!--//Lable con estado de guardado -->
	<p id="confirm1">No guardado</p><br>
	
	<div class="box_a">
	<?php
	for ($i = 0; $i < $numRega; $i++) {
	//Regar ahora
        echo "<button onclick='regarNow($i,5);' id='button_$i'>Encender ahora</button><br>";
    }
    ?>
    </div>

	<div class="box_b">
  	 <!-- // Boton para prender todos en secuencia-->
  	<button onclick="testAll();" id="prog2">Prender en secuencia</button> <br>

  	<label for='tiempoAll'>Tiempo (en minutos):</label>
  	<input type='number' id='tiempoAll' name='tiempoAll' value="5" min='1' max='100'><br><br>

  	<!-- // Boton para parar todo -->
  	<button onclick="offAll();" id="prog3">Parar todos</button> 
  	</div>
	
  	<!--
  	//Botones para futuras referencias
  	<button onclick="changeColor('yellow');">azul</button>
  	<button onclick="changeColor('red');">red</button> <br> <br>
  	<button onclick="testP('desdeAquí');">Fecha</button> <br> <br>
  	-->
	
<script src="script.js"></script> <!--// referencia al  script-->
</body>
</html>