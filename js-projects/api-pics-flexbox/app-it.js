// Méthode itérative

var nbItem = 50;
var picUrl = "";

// Récupérer l'URL d'un image 200*300
var picCard = document.querySelector(".users");
for (let i = 0; i < nbItem; i++) {
    fetch("https://picsum.photos/200/300").then(function (response) {
        picUrl = response.url;
        picCard.innerHTML += `<div class="item">
        <img src=${response.url} alt="photo ${response.url}"></img>
    </div>`;
        console.log(response);
    });
}
