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
    var boxOne1 = document.getElementsByClassName("question-box-two");
    var shadowBox1 = document.getElementsByClassName("background");
    if (n == 1) {
        boxOne1[0].classList.remove("qu-two-off");
        boxOne1[0].classList.add("qu-two-on");
        shadowBox1[0].style.display = "block";
    }
    if (n == 2) {
        boxOne1[0].classList.remove("qu-two-on");
        boxOne1[0].classList.add("qu-two-off");
        shadowBox1[0].style.display = "none";
    }
}

//============================ panel ==============================
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
    page[panelpage - 1].style.display = "inline-block";
    StyPanel[panelpage - 1].classList.add("border");
}

// ============================CHART ==========================
var xValues =  ["مهر","آبان","آذر","دی","بهمن","اسفند"] ;
// xValues.classList.add('chart-text-style')

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      lineTension: 0,
      data:[0,500,0,500,750],
      borderColor: "#EC6666",
      fill: false
    },{
      lineTension: 0,
      data: [375,390,350,0,250,],
      borderColor: "#79D2DE",
      fill: false
    },{
     lineTension: 0,
      data: [520,250,190,150,0,],
      borderColor: "#147AD6",
      fill: false
    }]
  },
  options: {
    legend: {display: false},
    scales: {
      yAxes: [{ticks: {min: 0, max:750}}],
   
    }
  }
});

