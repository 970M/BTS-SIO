// Méthode récursive

var nbItem = 5;

var picCard = document.querySelector(".users");
const getUrls = function (n) {
    if (n == 1) {
        fetch("https://picsum.photos/200/300").then(function (response) {
            picCard.innerHTML += `<div class="item"><img src=${response.url} alt="photo ${response.url}"></img></div>`;
        });
    } else {
        fetch("https://picsum.photos/200/300").then(function (response) {
            picCard.innerHTML += `<div class="item"><img src=${response.url} alt="photo ${response.url}"></img></div>`;
            getUrls(n - 1);
        });
    }
};

getUrls(nbItem);
