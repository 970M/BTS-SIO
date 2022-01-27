#!/usr/bin/python3
#
# @File : traiter_agile.py
#
# @Authors : Guillaume DAGUET
#            gd.guillaume.daguet@gmail.com
#            [+|]
#
# @Date : 12/10/2021
#
# @Version : V1.0
#
# @Synopsis : 
#       
#       Ouverture d'un fichier en lecture : open(fichier, "r")
#           => Méthodes readline()
#       Traiter les lignes de textes (replace(), lower(), split ...)
#       Ouverture d'un fichier en écriture : open(fichier, "w") ou open(fichier, "a")
#           => Méthode write()
#

# =============================================================================
# IMPORTATION DES LIBRAIRIES
# =============================================================================

import datetime                                                 # Module de fonction pour la date
import os                                                       # Module de fonction systeme

# =============================================================================
# DECLARATION DES VARIABLES GLOBALES
# =============================================================================

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat("-", "minutes")

### Configuration
repEntree = "workspace/database" # Chemin du repertoire d'entree
repSortie = "workspace/tmp" # Chemin du repertoire de sortie

nom_fichier = 'agile.txt'
#nom_fichier = 'villes_guadeloupe.csv'

fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier + '.res' # Chemin complet vers le fichier de sortie

mot = "pour"

# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================

def traiter_ligne(fichDesc, texte):
    """
    Ecrire le contenu de la variable texte dans le fichier identifié par fichDesc
    ssi elle contient l'expression stocké dans mot
    """

    if 'SLUG' not in texte :                      # Si texte ne contient pas 'SLUG' <=>  Ne pas traiter l'entête du fichier

        if mot in texte :                         # Ecrire dans le fichier si texte contient mot
            fichDesc.write(texte)
            
    else :
        fichDesc.write(texte) # Ecrire les champs de l'entête qui nous concerne


def lire_traiter_ecrire_fichier(fEntree, fSortie):
    """
    Ouvir le fichier fEntree, le parcourir ligne par ligne, appeler une fonction de traitement sur le contenu de 
    la ligne courante puis écrire le résultat dans le fichier de sortie fSortie
    """
    with open(fEntree, "r") as filin:  
        
        with open(fSortie, "w") as filout: 

            strLigne = filin.readline()  

            while strLigne != "" :                   
        
                # TRAITEMENT A FAIRE
                traiter_ligne(filout, strLigne)                 # Appel de la fonction de traitement

                strLigne = filin.readline()


##############################################################################
# MAIN : Partie principal du programme
##############################################################################

lire_traiter_ecrire_fichier(fichEntree, fichSortie)             # Appel de la fonction lire_traiter_ecrire_fichier()
print("\nfichier généré : \n", fichSortie)

#os.system("EDIT " + fichSortie)                                # Windows
#os.system("cat " + fichSortie)                                 # Unix