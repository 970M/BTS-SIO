#!/usr/bin/python3
#
# @File : csv_to_json_dic.py
#
# @Authors : Guillaume DAGUET
#            gd.guillaume.daguet@gmail.com
#            [+|]
#
# @Date : 18/10/2021
#
# @Version : V1.0
#
# @Synopsis : 
#       Conversion d'un fichier au format .csv vers le format JSON
#       Ouverture d'un fichier en lecture : open(fichier, "r")
#           => Méthodes csv.DictReader()
#       Traiter les lignes de tableau et le convertir en bloc json
#       Ouverture d'un fichier en écriture : open(fichier, "w")
#           => Méthode write()
#

# =============================================================================
# IMPORTATION DES LIBRAIRIES
# =============================================================================

import datetime                                                 # Module de fonction pour la date
import csv                                                      # Module de fonction systeme

# =============================================================================
# DECLARATION DES VARIABLES GLOBALES
# =============================================================================

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat("-", "minutes")

### Configuration
repEntree = "workspace/database" # Chemin du repertoire d'entree
repSortie = "workspace/tmp" # Chemin du repertoire de sortie

nom_fichier = 'villes_guadeloupe.csv'
nom_fichier = 'villes_france.csv'
nom_fichier_splited = nom_fichier.split(".")

fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier_splited[0] + '.json' # Chemin complet vers le fichier de sortie


# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================
     
def conversion_to_json(fEntree, fSortie):

    # Ouverture du fichier avec with open
    with open(fEntree, "r") as filin:
        # Stocker le fichier dans une liste de dico [{c1:v1,c2:v2} , , ..., ], [ , , ..., ], ..., [ , , ..., ]]
        ldFichier = list( csv.DictReader(filin, delimiter=";") )

    # Ouvrir le fichier de sortie
    with open(fSortie, "w") as filout:

        # Boucler sur toutes les lignes du fichier 
        for dicLigne in ldFichier:

            # Initialisation de la chaine de caractere jsBloc à ecrire dans le fichier de sortie
            jsBloc = "{\n"

            # # Ajouter à jsBloc l'ensemble 'clé':'valeur' de la 1ere colonne (sans la virgule)
            # jsBloc = jsBloc + "\"" + lstEntete[0] + "\":\"" + lstLigne[0] + "\""

            # Boucler sur toutes les colonnes (items) de la ligne
            for cle, valeur in dicLigne.items():
                # Ajouter à jsBloc, la virgule et le retour chariot pour l'ensemble précédent puis l'ensemble 'clé':'valeur' de la colonne courante
                jsBloc = jsBloc + "\"" + cle + "\":\"" + valeur + "\"" + ",\n"

            # Supprmier les carateres ",\n" que la boucler à placée en trop à la derniere ligne
            jsBloc = jsBloc[:-2] # toute la chaine sauf les 3 derniers caracteres
            # finaliser jsBloc
            jsBloc = jsBloc + "\n}\n"

            # Ecrire le bloc corespondant à la ligne courante dans le fichier JSON
            filout.write(jsBloc)

##############################################################################
# MAIN : Partie principal du programme
##############################################################################

conversion_to_json(fichEntree, fichSortie)
