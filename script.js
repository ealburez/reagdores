function changeColor(newColor) {
  var elem = document.getElementById('text1');
  elem.style.color = newColor;
}
function updateDate() {
  changeColor('black');
  var dt = new Date();
  var arreglo = document.getElementById("hora1").value.split(":")
  var delta = parseInt(document.getElementById("tiempo1").value);
  var stopTime
  var output 
  
  dt.setHours(parseInt(arreglo[0]));
  dt.setMinutes(parseInt(arreglo[1]));
  dt.setTime (dt.getTime() + delta*60000);
  stopTime = [dt.getHours(),dt.getMinutes()]

  if (stopTime[0]<10){
  	output = "0" + stopTime[0] + ":"
  } else {
  	output = stopTime[0] + ":"
  }
  if (stopTime [1]<10){
  	output += "0" + stopTime[1]
  } else {
  	output += stopTime[1]
  }
  document.getElementById("fecha0").innerHTML = dt.toLocaleString();
  document.getElementById("tiempo2").innerHTML = output;
  //document.getElementById("tiempo1").value = 10;
  //document.getElementById("hora1").value = "02:08"
  //document.getElementById("hora1").value = output
  
}
