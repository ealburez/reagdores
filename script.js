function changeColor(newColor) {
  var elem = document.getElementById('text1');
  elem.style.color = newColor;
}

function updateDate() {
  changeColor('black');
  //----Variables de html
  var numRega =  parseInt(document.getElementById("numRega").textContent)
  var delta;		//dieferencia de tiempo que debe ser
  var hora; 		//hora de inicio del riego
  
  // Otras variables
  var dt = new Date();
  var currentDate = new Date();
  var i = 1;
  var stopTime;
  var output;  
  var lista =["hora"]
  
  //poner el for aquí
  hora = document.getElementById("hora_"+i).value.split(":");
	delta = parseInt(document.getElementById("tiempo_"+i).value);

  dt.setHours(parseInt(hora[0]));
  dt.setMinutes(parseInt(hora[1]));
  dt.setTime(dt.getTime() + delta * 60000);
  stopTime = [dt.getHours(), dt.getMinutes()]

  if (stopTime[0] < 10) {
    output = "0" + stopTime[0] + ":"
  } else {
    output = stopTime[0] + ":"
  }
  if (stopTime[1] < 10) {
    output += "0" + stopTime[1]
  } else {
    output += stopTime[1]
  }
  
  document.getElementById("confirm1").innerHTML = "Guardado:" + currentDate.toLocaleString();
  document.getElementById("tiempo2").innerHTML = output;
  //document.getElementById("tiempo1").value = 10;
  //document.getElementById("hora1").value = "02:08"
  //document.getElementById("hora1").value = output
}

