<?php
require_once 'Voiture.php';

echo '<h1>Créer Voiture</h1>';


# POST
if (isset($_POST['marque']) && isset($_POST['immatriculation']) && isset($_POST['couleur'])) {

    $vehicule1 = new Voiture($_POST['marque'], $_POST['couleur'], $_POST['immatriculation']);
    $vehicule1->afficher();
}
