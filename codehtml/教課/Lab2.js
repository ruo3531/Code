document.write('<script hidden src = "../flag.js"></script>');
function cat() {
	var str = document.getElementById("Link").value;
	document.getElementById("goto").innerHTML = "<a href='" + str + "' >chick</a>";
}
var tmp = window.alert;
window.alert = function(s){  
    tmp(s);
    tmp(flag);
}
