
function myFunction() {
    var txt;
    var r = confirm("Hi There!\nWe will update you with more content in the future. \nThank you for subscribing!");
    if (r == true) {
    txt = "Have A Great Day!";
    } else {
    txt = "Maybe Next Time!";
    }
    document.getElementById("demo").innerHTML = txt;
}
