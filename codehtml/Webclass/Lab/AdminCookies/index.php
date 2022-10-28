<?php
    $FROM_INCLUDE = true;
    include("flag.php");
    $tmp = "hahahaYouAreNotAdmin";
    setcookie("Flag",$tmp, time()+3600*24);
    $msg = "You are not \"admin\"";

    if (isset($_COOKIE['Flag'])) {
        $str1 = $_COOKIE['Flag'];
        if ($str1 === "admin") {
            $msg = "Welcome admin, the Flag is ".$flag;
        }
    }
    echo $msg;
?>

