var body = document.body;
var cnt = 0, sum = 0;
function Check(t){
    var num = t.keyCode;
    // alert(num);
    switch(num){
        case 0x54:
        case 0x52:
        case 0x41:
        case 0x4C:
        case 0x45:
            sum++;
        break;
        // case 0x4C:
        //     sum++;
        // break;
        case 0x45:
            sum++;
        break;
        case 0x52:
            sum++;
        break;
        case 0x54:
            sum++;
        break;
    }
    console.log(sum);
}
body.addEventListener('keydown', Check ,false) 