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
    var habilita;

    // Otras variables
    var dt = new Date();
    var currentDate = new Date();
    var i;
    var stopTime;
    var output="";
  
  //poner el for aquí
    for (i=0;i<numRega;i++){
        
        if(document.getElementById("estado_"+i).checked){
            habilita=1;
        } else {
            habilita="";
        }
        
        hora = document.getElementById("hora_"+i).value.split(":");
        if (!document.getElementById("hora_"+i).value){
            hora=["12","00"];
            habilita="";
        }
            
        delta = parseInt(document.getElementById("tiempo_"+i).value);
        if (!document.getElementById("tiempo_"+i).value){
            delta=1;
            habilita="";
        }
        
        dt = new Date(); 
        dt.setHours(parseInt(hora[0]));
        dt.setMinutes(parseInt(hora[1]));
        dt.setTime(dt.getTime() + delta * 60000);
        stopTime = [dt.getHours(), dt.getMinutes()];

        output += i+","+habilita+","+hora[0]+":"+hora[1]+",";
        
        if (stopTime[0] < 10) {
            output += "0" + stopTime[0] + ":";
        } else {
            output += stopTime[0] + ":";
        }
        if (stopTime[1] < 10) {
            output += "0" + stopTime[1];
        } else {
            output += stopTime[1];
        }

        output+=","+delta+"\\n";
    }
     testP(output);
    
    document.getElementById("confirm1").innerHTML = "Guardado:" + currentDate.toLocaleString();
    document.getElementById("tiempo_2").innerHTML = output;
    alert('Configuración guardada =)');
    //Reload  the webpage to see the results
    location.reload();
    
   //document.getElementById("tiempo1").value = 10;
  //document.getElementById("hora1").value = "02:08"
  //document.getElementById("hora1").value = output
}

function testP(texto){
    var request = new XMLHttpRequest()
    request.open("GET","save.php?pic="+texto,true);
    request.send(null);
    return 0;
}

function regarNow(regadorID,timeSet){
    var request = new XMLHttpRequest()
    request.open("GET","save.php?water="+regadorID+"&tiempo="+timeSet,true);
    request.send(null);
    return 0;
}
//enciende todos los regadores uno detrás del otro
function testAll(){
    var request = new XMLHttpRequest()
    minutos=document.getElementById("tiempoAll").value;
    request.open("GET","save.php?tiempoTodos="+minutos,true);
    request.send(null);
    return 0;
}

//apaga todo los regadores enviando el parametro tiempo=0
function offAll(){
    var request = new XMLHttpRequest()
    request.open("GET","save.php?tiempoTodos=0",true);
    request.send(null);
    return 0;
}