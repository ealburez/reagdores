<?php
if (isset ($_GET["pic"])){
    $pic= strip_tags ($_GET["pic"]);
    system("printf '".$pic."'>regadores.conf");
    system("python mainRPI.py");


}
if((isset ($_GET["water"]))){
    $water= strip_tags ($_GET["water"]);
    $tiempo= strip_tags ($_GET["tiempo"]);
    system("python water.py ".$tiempo." ".$water);
}

if((isset ($_GET["tiempoTodos"]))){
    $tiempoTodos= strip_tags ($_GET["tiempoTodos"]);
    system("python water.py ".$tiempoTodos);
}
?>
