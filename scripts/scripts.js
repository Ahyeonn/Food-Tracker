// Alert
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

// Audio Play
var mySong = document.getElementById("mySong");
var icon = document.getElementById("icon");

icon.onclick = function(){
    if(mySong.paused){
        mySong.play();
        icon.src = "./images/pause.png"
    }else{
        mySong.pause();
        icon.src = "./images/play.png"
    }
}

// Men's Calorie 
const menWeight = document.querySelector('#men-weight');
const menHeight = document.querySelector('#men-height');
const menAge = document.querySelector('#men-age');
const menPhysical = document.querySelector('#men-physical-activity');
const menCalorie = document.querySelector('#men-calorie');

document.getElementById("men-submit").addEventListener("click", updateMenCalorie);

function updateMenCalorie() {
    const physicalActivity = menPhysical.value;
    let defaultNum = 1;
    if (physicalActivity == "Little or no exercise"){
        defaultNum = 1.2;
    }
    if (physicalActivity == "Exercise 1-3 days/week"){
        defaultNum = 1.375;
    }
    if (physicalActivity == "Exercise 3-5 days/week"){
        defaultNum = 1.55;
    }
    if (physicalActivity == "Exercise 6-7 days/week"){
        defaultNum = 1.725;
    }
    if (physicalActivity == "hard exercise 6-7 days/week"){
        defaultNum = 1.9;
    }

    const newMenTotal = 66.47 + (13.75 * menWeight.value)+(5.003 * menHeight.value)-(6.755 * menAge.value)
    const menWithPhysical = parseInt(newMenTotal * defaultNum)
    menCalorie.innerHTML = menWithPhysical

  document.getElementById("men-calorie").innerHTML = menWithPhysical;
}

// Women's Calorie
const womenWeight = document.querySelector('#women-weight');
const womenHeight = document.querySelector('#women-height');
const womenAge = document.querySelector('#women-age');
const womenPhysical = document.querySelector('#women-physical-activity');
const womenCalorie = document.querySelector('#women-calorie');

document.getElementById("women-submit").addEventListener("click", updateWomenCalorie);

function updateWomenCalorie() {
    const physicalActivity = womenPhysical.value;
    let defaultNum = 1;
    if (physicalActivity == "Little or no exercise"){
        defaultNum = 1.2;
    }
    if (physicalActivity == "Exercise 1-3 days/week"){
        defaultNum = 1.375;
    }
    if (physicalActivity == "Exercise 3-5 days/week"){
        defaultNum = 1.55;
    }
    if (physicalActivity == "Exercise 6-7 days/week"){
        defaultNum = 1.725;
    }
    if (physicalActivity == "hard exercise 6-7 days/week"){
        defaultNum = 1.9;
    }

    const newWomenTotal = 655.1 + (9.563 * womenWeight.value)+(1.850 * womenHeight.value)-(4.676 * womenAge.value)
    const womenWithPhysical = parseInt(newWomenTotal * defaultNum)
    womenCalorie.innerHTML = womenWithPhysical

  document.getElementById("women-calorie").innerHTML = womenWithPhysical;
}