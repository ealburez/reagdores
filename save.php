<?php
if (isset ($_GET["pic"])){
    $pic= strip_tags ($_GET["pic"]);
    system("printf '".$pic."'>regadores.conf");


}
if((isset ($_GET["water"]))){
    $water= strip_tags ($_GET["water"]);
    system("echo '".$water."' > algo2.txt");
}
?>