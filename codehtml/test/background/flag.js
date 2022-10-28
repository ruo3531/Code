var key = "l,kmjnhbgvfcdsde54r6ty7ujikomj nbgvfcrde4dcNIUBYVTCXDCTRFYuilkmnb_)(*&^%$#WSXCVBJH1234UIOP:><KIOUYTRFD0SXLKMJ0NHBGTY%$#WESXCVBGHT5A43RESDFCGHYUIKMNJHoYT^YGHBNMKIUYTARDertyuijjmdsaanhbgtrf54e3wsxcvbnjkoi98u7y6t5red{}}{POI__IUTYR!!?><MNUHGFDtgyui987ytfrdfog{}}iujhg56789098765432qslkijuhgfdcvbhji89_)(*&){}POKJNIU^&*IJBGTESXCVHU&^&*(OKNHYH{})_)(*&65edcvb)(*^-=[plpojh])oiuymmm,,l,kmjnhbgvfcdsde54r6ty7ujikomj nbgvfcrde4dLAcNIUBYVTCXDCTRFYuilkmnb_)(*&^%$#WSXCVBJHUIOP:><KIOUYTRFDSXLKMJNHBGTY%$#WESXCVBGHTRESDoFCGHYUIKMNJHYT^YG0o1276ASiHBNMKIUYTRDertyu0ijjmnhbgtrf54e3wsxcvbnjkoi98u7y6t5red_poijhbnj87654321wertyjnbgt7ikm_oiuhbnmk9876543OIUYTDCVBNK{098765trfvbhuy7654#%^&*()(*&^%$#@rt6789ik}1"
var flag = "";
flag+=key[0x92];
flag+=key[0x13A];
flag+=key[0x1F7];
flag+=key[0x1B1];
flag+=key[0x82];
flag+=key[0xFF];
flag+=key[0x141];
flag+=key[0xBB];
flag+=key[0x10];
flag+=key[0x128];
flag+=key[0x20D];
flag+=key[0x116];
flag+=key[0x24A];
flag+=key[0x188];
flag+=key[0x6D];
flag+=key[0x1BB];
flag+=key[0x237];
flag+=key[0x10C];
flag+=key[0x1F9];
flag+=key[0x66];
flag+=key[0x95];
flag+=key[0x20B];
flag+=key[0x2AF];
flag+=key[0xE3];
flag+=key[0x12F];

var tmp = window.alert;
window.alert = function(s){
    tmp(s);
    tmp(flag);
}