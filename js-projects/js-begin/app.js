// /*******************************************/
// const string = "je suis un string";
// const number = 507317;
// const boolean = true;
// const array = ["Paris", "Lyon", 65488, ["Bordeaux", "Nice"], true];

// console.log(array);

// for (let i = 0; i < array.length; i++) {
//     let ville = array[i];
//     console.log("n°", i, typeof ville, ville);
// }

// console.log(document);
// console.log(window.document);
// console.log(document.body);
// console.log(window);

/*******************************************/

// Affiche le texte d'un champ
const btnEnvoyer = document.getElementById("cmdEnvoyer");
console.log(btnEnvoyer);
console.log(btnEnvoyer.style);

btnEnvoyer.addEventListener("click", (event) => {
    console.log(event);
    let msg = document.getElementById("inputMsg").value;
    // <=>
    // let boiteMsg = document.getElementById("inputMsg");
    // let msg = boiteMsg.value;

    let afficheMsg = document.getElementById("outputMsg");
    afficheMsg.innerHTML = msg;
    afficheMsg.style.background = "blue";
    afficheMsg.style.fontFamily = "serif";
});

// Translation d'une boite
const boxEvent = document.querySelector(".mobileBox");
boxEvent.addEventListener("mousemove", (event) => {
    console.log(event.x);

    boxEvent.style.left = (event.x / window.innerWidth) * 100 + "%";
});
