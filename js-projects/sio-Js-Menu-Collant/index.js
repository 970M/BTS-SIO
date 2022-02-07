(function () {
    /* Lorsque que l'on scroll :
        Si le menu sort de l'ecran alors il deviendra fixe
    */
    var element = document.querySelector(".menu");
    // Detecter la position du menu par rapport à l'écran : element.getBoundingClientRect()
    var rect = element.getBoundingClientRect();
    var top = rect.top + window.scrollY;

    var onScroll = function () {
        console.log("position=", rect.top);
        console.log("scrollY=", window.scrollY);
        console.log("top=", top);

        // Creer un élément fake
        var fake = document.createElement("div");
        fake.style.with = rect.width + "px";
        fake.style.height = rect.height + "px";

        if (window.scrollY > top) {
            element.classList.add("fixed");
            element.style.width = rect.width + "px";
            // Recuperer l'élément parent et lui ajout fake avant element
            element.parentNode.insertBefore(fake, element);
        } else if (window.scrollY <= top) {
            element.classList.remove("fixed");
            element.parentNode.removeChild(fake);
        }
    };
    window.addEventListener("scroll", onScroll);
})();
