function maxLengthCheck(object) {
    if(object.value.length > object.maxLength)
        object.value = object.value.slice(0,object.maxLength)
}
   
function passwordShowText(){
    var x = document.getElementById("passwordId")
    if (x.type == "password")
        x.type = "text"
    else
        x.type  = "password"  
}
