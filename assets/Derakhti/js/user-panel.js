//======================= trash alert ==================================

function trash(n) {
    var boxOne = document.getElementsByClassName("question-box");
    var shadowBox = document.getElementsByClassName("background");
    if (n == 1) {
        boxOne[0].classList.remove("qu-off");
        boxOne[0].classList.add("qu-on");
        shadowBox[0].style.display = "block";
    }
    if (n == 2) {
        boxOne[0].classList.remove("qu-on");
        boxOne[0].classList.add("qu-off");
        shadowBox[0].style.display = "none";
    }
}

// =================================== close ======================
function exit(n) {
    console.log(1);
    var boxOne1 = document.getElementById("qu-two-on");
    // var shadowBox1 = document.getElementsByClassName("background");
    if (n == 1) {
        // boxOne1[0].classList.remove("qu-two-off");
        // boxOne1[0].classList.add("qu-two-on");
        boxOne1.style.display = "block";
    }
    if (n == 2) {
        // boxOne1[0].classList.remove("qu-two-on");
        // boxOne1[0].classList.add("qu-two-off");
        boxOne1.style.display = "none";
    }
}

var panelpage = 1;
panel(1);




function SelectPanel(n) {
    panel(panelpage = n);
}

function panel(n) {
    var i;
    var page = document.getElementsByClassName("panel-page");
    var StyPanel = document.getElementsByClassName("panels-details");
    if (n > page.length) { panelpage = 1 }
    if (n < 1) { panelpage = page.length }
    for (i = 0; i < page.length; i++) {
        page[i].style.display = "none";
    }
    for (i = 0; i < StyPanel.length; i++) {
        StyPanel[i].classList.remove("border");
    }
    page[panelpage - 1].style.display = "grid";
    StyPanel[panelpage - 1].classList.add("border");
}
