#!/usr/bin/python3
#
# @File : csv_to_json.py
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
#           => Méthodes csv.reader()
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
nom_fichier_splited = nom_fichier.split(".")

fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier_splited[0] + '.json' # Chemin complet vers le fichier de sortie


# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================
     
def conversion_to_json(fEntree, fSortie):

    # Ouverture du fichier avec with open
    with open(fEntree, "r") as filin:
        # Stocker le fichier dans une liste de liste [[ , , ..., ], [ , , ..., ], ..., [ , , ..., ]]
        lst2DFichier = list( csv.reader(filin, delimiter=";") )

    # Récupérer les noms des colonnes dans la premiere ligne
    lstEntete = lst2DFichier[0]

    # Ouvrir le fichier de sortie
    with open(fSortie, "w") as filout:

        # Boucler sur toutes les lignes du fichier sauf la premiere
        for i in range(1, len(lst2DFichier)):

            # Recuperer la ligne courante
            lstLigne = lst2DFichier[i]

            # Initialisation de la chaine de caractere jsBloc à ecrire dans le fichier de sortie
            jsBloc = "{\n"

            # Ajouter à jsBloc l'ensemble 'clé':'valeur' de la 1ere colonne (sans la virgule)
            jsBloc = jsBloc + "\"" + lstEntete[0] + "\":\"" + lstLigne[0] + "\""

            # Boucler sur toutes les colonnes de la ligne
            for j in range(1, len(lstLigne)):

                # Ajouter à jsBloc, la virgule et le retour chariot pour l'ensemble précédent puis l'ensemble 'clé':'valeur' de la colonne courante
                jsBloc = jsBloc + ",\n\"" + lstEntete[j] + "\":\"" + lstLigne[j] + "\""

            # finaliser jsBloc
            jsBloc = jsBloc + "\n}\n"

            # Ecrire le bloc corespondant à la ligne courante dans le fichier JSON
            filout.write(jsBloc)

##############################################################################
# MAIN : Partie principal du programme
##############################################################################

conversion_to_json(fichEntree, fichSortie)
