var Png = document.getElementById("Pic");
var Out = document.getElementById("Output");
var Color = ["#feaad3","#b4dbfb","#ffe484","#9ccf9c","000000"]
var num = 1;
Png.addEventListener('click', function(){
    if(document.getElementById("Input").value != "" && document.getElementById("Input").value != null){
        num = document.getElementById("Input").value;
        document.getElementById("Input").value = "";
    }
    else num = (num%4)+1;
    Out.style.color = Color[num-1];
    Png.src = "img/"+num+".png";
})
Png.addEventListener('load', function(){
    Out.innerHTML = "You Find No."+num+" cat!!!";
})
Png.addEventListener('error', function(){
    Out.innerHTML = "You Can't Find No."+num+" catQQ";
    // num = 5;
})