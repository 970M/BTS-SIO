// "use strict";

// const string = "je suis un string";
// const number = 507317;
// const boolean = true;
// const array = ["Paris", "Lyon", 65488, ["Bordeaux", "Nice"], true];

// console.log(array);

// for (let i = 0; i < array.length; i++) {
//     let ville = array[i];

//     console.log("n°", i, typeof ville, ville);

//     // for (let i = 0; i < ville.length; i++) {
//     //     console.log(ville[i]);
//     // }

//     let j = 0;
//     Array.from(ville).forEach((element) => {
//         console.log("  sn°", i, j, typeof element, element);
//         j++;
//     });
// }

// // Trier un tableau de chiffres
// let numbers = [15, 2, 69, 84, 3, 152, 9];
// console.log(numbers.sort((a, b) => a - b));

// //*********************************************************************/
// // Manipulation de l'objet Window
// //*********************************************************************/

// console.log("L'objet window", window);

// var vp = window.prompt("Salut les gens (prompt) !!!");
// var vc = window.confirm("Salut les gens (confirm) !!!");

//*********************************************************************/
// Manipulation du DOM
//*********************************************************************/

// Affiche le texte d'un champ
const btnEnvoyer = document.getElementById("cmdEnvoyer");
btnEnvoyer.addEventListener("click", (event) => {
    console.log(event.target.value);
    var msg = document.getElementById("inputMsg").value;
    var afficheMsg = document.getElementById("outputMsg");
    afficheMsg.innerHTML = msg;
    afficheMsg.style.background = "blue";
    afficheMsg.style.fontFamily = "serif";
    alert(msg);
});

// Ré-écriture d'un texte
document.getElementById("ecrireMsg").addEventListener("input", (event) => {
    console.log(event.target.value);
    var msg = document.getElementById("ecrireMsg").value;
    var afficheMsg = document.getElementById("outputMsg");
    afficheMsg.innerHTML = msg;
    afficheMsg.style.background = "red";
    afficheMsg.style.border = "solid 5px yellow";
    afficheMsg.style.fontFamily = "sans";
});

// Translation d'une boite
const boxEvent = document.querySelector(".mobileBox");
boxEvent.addEventListener("mousemove", (event) => {
    console.log(event.x);

    boxEvent.style.left = (event.x / window.innerWidth) * 100 + "%";
});

// **********************************************************
// **********************************************************
// Mode decomposé (affiche le message sans cliquer!!!)
// var envoyerMsg = function () {
//     //console.log();
//     var msg = document.getElementById("inputMsg").value;
//     afficheMsg = document.getElementById("outputMsg");
//     afficheMsg.innerHTML = msg;
//     afficheMsg.style.background = "blue";
//     afficheMsg.style.fontFamily = "sans";
//     alert(msg);
// };
// const btnEnvoyer = document.getElementById("cmdEnvoyer");
// btnEnvoyer.addEventListener("click", (event) => {
//     console.log(event.target.value);
//     envoyerMsg();
// });
// **********************************************************
// // Mode compact
// document.getElementById("cmdEnvoyer").addEventListener("click", function () {
//     var msg = document.getElementById("inputMsg").value;
//     alert(msg);
// });
// // Mode compact fléché qui fonctionne
// document.getElementById("cmdEnvoyer").addEventListener("click", () => {
//     var msg = document.getElementById("inputMsg").value;
//     alert(msg);
// });
