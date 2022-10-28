<?php
    highlight_file(__FILE__);
    $FROM_INCLUDE = true;
    include("flag.php");
    $msg = "Keep trying!";
    if (isset($_GET['user']) && isset($_GET['password'])) {
        $str1 = $_GET['user'];
        $str2 = $_GET['password'];
        if ($str1 === "admin"  && $str2 === "ji32k7au4a83") {
            $msg = "Flag: ".$flag;
        }
    }
    echo $msg;
?>

