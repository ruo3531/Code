<?php
    $FROM_INCLUDE = true;
    include("flag.php");
    setcookie("Flag",$flag, time()+3600*24);
    $msg = "Can you find me?";
    echo $msg;
?>

