<?php
    highlight_file(__FILE__);
    $FROM_INCLUDE = true;
    include("flag.php");
    $msg = "Keep trying!";
    if (isset($_POST['user']) && isset($_POST['password'])) {
        $str1 = $_POST['user'];
        $str2 = $_POST['password'];
        if ($str1 === "admin"  && $str2 === "HelloNI5R@") {
            $msg = "Flag: ".$flag;
        }
    }
    echo $msg;
?>

