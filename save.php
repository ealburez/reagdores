<?php
if (isset ($_GET["pic"])){
    $pic= strip_tags ($_GET["pic"]);
    system("printf '".$pic."'>regadores.conf");
    system("python mainRPI.py");


}
if((isset ($_GET["water"]))){
    $water= strip_tags ($_GET["water"]);
    system("python water.py 0.5 ".$water);
}

if((isset ($_GET["tiempoTodos"]))){
    $water= strip_tags ($_GET["tiempoTodos"]);
    system("python water.py ".$tiempoTodos);
}
?>
