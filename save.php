<?php
if (isset ($_GET["pic"])){
    $pic= strip_tags ($_GET["pic"]);
    system("printf '".$pic."'>regadores.conf");


}
if((isset ($_GET["water"]))){
    system("touch algo2.txt");
}
?>
