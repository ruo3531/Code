var Png = document.getElementById("Pic");
var Out = document.getElementById("Output");
var Color = ["#feaad3","#b4dbfb","#ffe484","#9ccf9c","000000"]
var num = 1;
Png.addEventListener('click', function(){
    num = (num%4)+1;
    if(document.getElementById("Input").value != ""){
        num = document.getElementById("Input").value;
        document.getElementById("Input").value = "";
    }
    Out.style.color = Color[num-1];
    Png.src = "img/"+num+".png";
    
})
Png.addEventListener('load', function(){
    Out.innerHTML = "Success";
})
Png.addEventListener('error', function(){
    Out.innerHTML = "Error";
    alert("Error");
})