console.log("toto");

fetch("https://api.blablagues.net/?rub=blagues")
    .then((res) => res.json())
    .then((resData) => {
        console.log(resData.data.content);

        const jHeader = document.getElementById("header");
        const jContent = document.getElementById("content");

        jHeader.textContent = resData.data.content.text_head;
        // ~<=> jHeader.innerHTML = resData.data.content.text_head;

        if (resData.data.content.text != "") {
            jContent.textContent = resData.data.content.text;
        } else {
            jContent.textContent = resData.data.content.text_hidden;
        }
    });

// // Avec définiton classique de fonction
// https: fetch("https://api.blablagues.net/?rub=blagues")
//     .then(function (response) {
//         // console.log(response.json());
//         return response.json();
//     })
//     .then(function (data) {
//         console.log("blague :", data);
//     });

// // Avec des fonctions flêchées
// fetch("https://randomuser.me/api/")
//     .then((response) => {
//         return response.json();
//     })
//     .then((data) => {
//         console.log("user :", data.results);
//     });

// ****************************************************
// Banque d'API
// ****************************************************

// Random users
fetch("https://randomuser.me/api/")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log("user :", data);
    });

// Photos de chats
fetch("https://api.thecatapi.com/v1/images/search")
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log("cat :", data);
    });

// Images aléatoires
fetch("https://picsum.photos/200/300").then((response) => {
    console.log(response);
    console.log("pic :", response.url);
});
