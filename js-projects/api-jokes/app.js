var getJoke = function () {
    fetch("https://api.blablagues.net/?rub=blagues")
        .then(function (response) {
            // console.log(response.json());
            return response.json();
        })
        .then(function (data) {
            console.log("blague :", data.data.content);

            var header = document.getElementById("header");
            var content = document.getElementById("content");

            header.textContent = data.data.content.text_head;
            // header.innerHTML = data.data.content.text_head;

            if (data.data.content.text == "") {
                content.textContent = data.data.content.text_hidden;
            } else {
                content.textContent = data.data.content.text;
            }

            console.log(header);
        });
};

getJoke();

var myButton = document.getElementById("my-button");

myButton.addEventListener("click", function (event) {
    console.log(event);
    getJoke();
});
