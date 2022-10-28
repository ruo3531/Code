var Input = document.getElementById('Input');
var Button = document.getElementById('Button');
var Outcome = document.getElementById('Output');

Button.addEventListener('click', function(){
    Outcome.innerText = Input.value;
    Input.value = "";
})
var tmp = window.alert;
window.alert = function(s){
    tmp(s);
    tmp("flag");
}
