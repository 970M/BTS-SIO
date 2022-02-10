<?php


# GET
if (isset($_GET['nom']) && isset($_GET['fonction'])) {
    // on affiche nos résultats
    echo 'Votre nom est ' . $_GET['nom'] . ' et votre fonction est ' . $_GET['fonction'] . '<br>';
}

# POST
if (isset($_POST['nom']) && isset($_POST['fonction'])) {
    // on affiche nos résultats
    echo 'Votre nom est ' . $_POST['nom'] . ' et votre fonction est ' . $_POST['fonction'] . '<br>';
}
