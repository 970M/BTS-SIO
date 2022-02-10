<?php

class Voiture
{

    private $marque;
    private $couleur;
    private $immatriculation;


    // --- Marque ---
    // un getter      
    public function getMarque()
    {
        return $this->marque;
    }

    // un setter 
    public function setMarque($m)
    {
        $this->marque = $m;
    }

    // --- Couleur ---
    // un getter      
    // To do ...

    // un setter
    // To do ...

    // --- Immatriculation ---
    // un getter      
    // To do ...

    // un setter 
    // To do ...

    // un constructeur
    public function __construct($m, $c, $i)
    {
        $this->marque = $m;
        $this->couleur = $c;
        $this->immatriculation = $i;
    }

    // une methode d'affichage.
    public function afficher()
    {
        // To do ...
    }
}


// $vehicule1 = new Voiture("Dacia", "Rouge", "152548");
// $vehicule1->afficher();

// // ---
// $prenom = "Helmut";
// echo <<< EOT
// Texte à afficher
// sur plusieurs lignes
// avec caractères spéciaux \t \n
//  et remplacement de variables $prenom
// les caractères suivants passent : " ' $ / \ ;
// EOT;
