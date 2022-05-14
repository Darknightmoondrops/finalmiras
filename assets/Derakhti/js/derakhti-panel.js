// var config = {
//         container: "#custom-colored",

//         nodeAlign: "BOTTOM",

//         connectors: {
//             type: 'curve'
//         },
//         node: {
//             HTMLclass: 'nodeExample1'
//         },

//     },
//     user1 = {
//         HTMLclass: 'light-gray',
//         text: {
//             title: "arian",
//             name: "",
//         }
//     },
//     user2 = {
//         parent: user1,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Head of Project Office",
//             name: "Name Surname",
//         }
//     },
//     user3 = {
//         parent: user1,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Head of IT Ops",
//             name: "Name Surname",
//         }
//     },
//     user4 = {
//         parent: user2,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Head of Development",
//             name: "Name Surname",
//         }
//     },
//     user5 = {
//         parent: user2,

//         HTMLclass: 'light-gray',
//         text: {
//             title: "Head of Portfolio",
//             name: "Name Surname",
//         }
//     },
//     user6 = {
//         parent: user3,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Vision",
//             name: "Name Surname",
//         }
//     },
//     user7 = {
//         parent: user3,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Staff / Skills",
//             name: "Name Surname",
//         }
//     },
//     user8 = {
//         parent: user4,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Project Management",
//             name: "Name Surname"
//         }
//     },
//     user9 = {
//         parent: user4,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Application Support",
//             name: "Name Surname"
//         }
//     },
//     user10 = {
//         parent: user5,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Cybersecurity",
//             name: "Name Surname"
//         }
//     },
//     user11 = {
//         parent: user5,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Infrastructure",
//             name: "Name Surname"
//         }
//     },
//     user12 = {
//         parent: user6,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Management Information",
//             name: "Name Surname"
//         }
//     },
//     user13 = {
//         parent: user6,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Service Desk",
//             name: "Name Surname"
//         }
//     },
//     user14 = {
//         parent: user7,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Tech Services",
//             name: "Name Surname"
//         }
//     },
//     user15 = {
//         parent: user7,
//         HTMLclass: 'light-gray',
//         text: {
//             title: "Research & Development",
//             name: "Name Surname"
//         }
//     },
//     chart_config = [
//         config,
//         user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12, user13, user14, user15
//     ];

// new Treant(chart_config);

// siblingSeparation: 20;
// subTeeSeparation: 20;
// padding: 10;

//======================= chaert part ========================
//======================= chart two ============

var xValuesTwo = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"];

new Chart("myChartTwo", {
    type: "line",
    data: {
        labels: xValuesTwo,
        datasets: [{
                data: [0, 500, 0, 0, 750, 0, 0, 0, 0, 0, 0, 0],
                borderColor: "rgb(155, 155, 255)",
                fill: false
            },
            {
                data: [0, 200, 0, 0, 500, 0, 0, 0, 0, 0, 0, 0],
                borderColor: "orange",
                fill: false
            }
        ]
    },
    options: {
        legend: { display: false },
        scales: {
            yAxes: [{ ticks: { min: 0, max: 750 } }],

        }
    }
});
//======================= END chaert part =====================
// var page1 = 1;

// function SelectPanel(n) {
//     panel(panelpage = n);
// }

// function panel(n) {
//     var i;
//     var page = document.getElementsByClassName("panel-page");
//     var StyPanel = document.getElementsByClassName("panels-details");
//     var treantChart = document.getElementById('custom-colored');
//     if (n > page.length) { panelpage = 1 }
//     if (n < 1) { panelpage = page.length }
//     for (i = 0; i < page.length; i++) {
//         page[i].style.display = "none";
//     }
//     for (i = 0; i < StyPanel.length; i++) {
//         StyPanel[i].classList.remove("border");
//     }
//     if (n == 4) {
//         treantChart.style.display = "block";
//     } else {
//         treantChart.style.display = "none";
//     }
//     page[panelpage - 1].style.display = "block";
//     StyPanel[panelpage - 1].classList.add("border");
// }