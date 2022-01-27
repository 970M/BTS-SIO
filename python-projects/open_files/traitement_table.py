#!/usr/bin/python3
#
# @File : traitement_table.py
#
# @Authors : Guillaume DAGUET
#            gd.guillaume.daguet@gmail.com
#            [+|]
#
# @Date : 20/10/2021
#
# @Version : V1.0.0
#
# @Synopsis : 
#       Import de fichier CSV
#       Selection de ligne en table suivant des criteres
#       Jointure de table
#

# =============================================================================
# IMPORTATION DES LIBRAIRIES
# =============================================================================

import datetime                                                 # Module de fonction pour la date
import csv                                                      # Module de fonction d'ouverture/ecriture de .csv

# =============================================================================
# DECLARATION DES VARIABLES GLOBALES
# =============================================================================

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat("-", "minutes")

### Configuration
repEntree = "workspace/database" # Chemin relatif du repertoire d'entree
repSortie = "workspace/tmp" # Chemin relatif du repertoire de sortie

fichier_eleves = 'eleves.csv'
fichier_note = 'notes.csv'
fichier_bulletin = 'bulletin.csv'

fileIn_Eleves = repEntree + '/' + fichier_eleves # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fileIn_Notes = repEntree + '/' + fichier_note # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)

fileOut_Bulletin = repSortie + '/' + fichier_bulletin # Chemin complet vers le fichier de sortie

# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================

# Fusionner 2 lignes de dictionnaire en une seule
def fusion(e, n):

    return {"prénom": e["prénom"], "jour": e["jour"], "mois": e["mois"], "année": e["année"], "projet": e["projet"], "note": n["note"]}

# Ecrire une liste de dictionnaire dans un fichier au format.csv
def ecrire_csv_dic(csvFile, tabData, sep):

    with open(csvFile, 'w') as filout:

        wobj = csv.DictWriter(filout, fieldnames=tabData[0].keys(), delimiter=sep)
        wobj.writeheader()
        wobj.writerows(tabData)


# Générer un fichier .csv correspondant à la jointure de 2 autres fichier .csv
def joint_eleves_notes(csvEl, csvNo, csvSortie):
    # Ouvrir le fichier eleves.csv
    with open (csvEl, "r") as filinE:
        tabEleves = list(csv.DictReader(filinE, delimiter=","))       # renvoi une liste de dictionnaires

    # Ouvrir le fichier notes.csv
    with open (csvNo, "r") as filinN:
        tabNotes = list(csv.DictReader(filinN, delimiter=","))       # renvoi une liste de dictionnaires

    print("tabEleves :")
    for i in tabEleves:
        print(i)

    print("tabNotes :")
    for i in tabNotes:
        print(i)

    # Initialisation du tableau contenant les données à ecrire dans le fichier de sortie
    tabBulletin=[]
    # Parcourir les éléves
    for el in tabEleves:
        # Parcourir les notes
        for no in tabNotes:
            # Le prenom de l'eleve coincide avec le prenom associé à la note
            if el["prénom"] == no["prénom"]:
                tabBulletin.append(fusion(el,no))

    # Ecrire au format .csv dans le fichier de sortie
    ecrire_csv_dic(csvSortie, tabBulletin, ",")

##############################################################################
# MAIN : Partie principal du programme
##############################################################################
joint_eleves_notes(fileIn_Eleves, fileIn_Notes, fileOut_Bulletin)