// Méthode await/async

var nbItem = 20;
var picUrls = [];

const getUrls = async function (n) {
    for (let i = 0; i < n; i++) {
        await fetch("https://picsum.photos/200/300").then(function (response) {
            picUrls.push(response.url);
            console.log(picUrls);
        });
    }
};

const injectHtml = function () {
    var picCard = document.querySelector(".users");
    for (let i = 0; i < nbItem; i++) {
        console.log("affiche:", i, picUrls[i]);
        picCard.innerHTML += `<div class="item">
            <img src=${picUrls[i]} alt="photo ${picUrls[i]}"></img>
        </div>`;
    }
};

const displayPic = async function () {
    await getUrls(nbItem);
    injectHtml();
};

displayPic();
// **************************
//    A FAIRE
// **************************

// 1- Ecrire une fonction qui, un nombre nbItem de fois,
// récupere une URL via l'api et la push dans un tableau.

// 2- Ecrire une fonction qui, pour chacun des éléments
// du tableau d'URL (nbItem de fois), injecte le code
// <div class="item"><img src=${<pic_url>} alt="photo ${<pic_url>}"></img></div>
// dans le fichier html.
// <pic_url> doit être remplacée par l'url des images contenu dans le tableau
