#!/usr/bin/python3
#
# @File : ouvrir_csv.py
#
# @Authors : Guillaume DAGUET
#            gd.guillaume.daguet@gmail.com
#            [+|]
#
# @Date : 12/10/2021
#
# @Version : V1.0.0
#
# @Synopsis : 
#       
#       Ouverture d'un fichier .csv en lecture :
#           => Méthodes ...
#       fonction de traitement de ligne de texte (replace(), lower() ...)
#       Générer un fichier .csv à artir d'un tableau (liste de liste) : 
#           => Méthode ...
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

nom_fichier = 'villes_guadeloupe.csv'
#nom_fichier = 'villes_guadeloupe_no-header.csv'

fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier + '.' + date # Chemin complet vers le fichier de sortie

# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================

# -------------------------------------
# [[ csv.reader() / csv.writer() ]]
# -------------------------------------

### reader(): Ouvrir un fichier .csv et le stocker dans une liste de listes (un tableau 2D)
def ouvrir_csv_lst(csvFile):

    with open (fichEntree, "r") as filin:

        lst2DFichier = list( csv.reader(filin, delimiter=";") )

    #print(lst2DFichier)
    return lst2DFichier

# INFO :
# lst2DFichier[ligne][colonne] :
# lst2DFichier => [[ID,DEP,SLUG,NOM,NOM_SIMPLE,CODE_POSTAL], [36569,971,les-abymes,ABYMES,les abymes,97142], ..., [36828,971,st-martin,SAINT MARTIN,st martin,97150]]
# lst2DFichier[0] => [ID,DEP,SLUG,NOM,NOM_SIMPLE,CODE_POSTAL]
# lst2DFichier[1][3] => "ABYMES"


### writer(): Ecrire un fichier .csv avec le module csv
def ecrire_csv_lst2D(csvFile, tabData):

    with open(csvFile, 'w') as filout:

        wobj = csv.writer(filout, delimiter=";")
        wobj.writerows(tabData)

# -------------------------------------
# [[ csv.DictReader() / csv.DictWriter() ]]
# -------------------------------------

### DictReader(): Ouvrir un fichier .csv et le stocker dans une liste de dictionnaire :
#
#  Un fichier .csv de k lignes et n colonnes sera stocké comme-ci:
#
#  [{'K1.1':'V1.1', ..., 'K1.n':'V1.n'},                        # ligne n°1 du fichier
#   {'K2.1':'V2.1', ..., 'K2.n':'V2.n'},                        # ligne n°2 du fichier
#   ...                                ,                        # ...
#   {'Kk.1':'Vk.1', ..., 'Kk.n':'Vk.n'}]                        # ligne finale n°k du fichier
#  
def ouvrir_csv_dic(csvFile):

    with open (fichEntree, "r") as filin:

        ldFichier = list(csv.DictReader(filin, delimiter=";"))       # renvoi une liste de dictionnaires

    return ldFichier

### DictWriter(): Ecrire un fichier .csv avec le module csv
def ecrire_csv_dic(csvFile, dicData):

    with open(csvFile, 'w') as filout:

        wobj = csv.DictWriter(filout, fieldnames=dicData[0].keys(), delimiter=";")
        wobj.writeheader()
        wobj.writerows(tabData)


##############################################################################
# MAIN : Partie principal du programme
##############################################################################

# -------------------------------------
# [[ csv.reader() / csv.writer() ]]
# -------------------------------------

tabCSV = ouvrir_csv_lst(fichEntree)

print("Affichage tableau:")
print(tabCSV)

print("\nAffichage ligne par ligne:")
for ligne in tabCSV:
    print(ligne)


### Ecriture d'une liste de liste dans fichier au format .csv
ecrire_csv_lst2D(fichSortie, tabCSV)


# -------------------------------------
# [[ csv.DictReader() / csv.DictWriter() ]]
# -------------------------------------

# dicCSV = ouvrir_csv_dic(fichEntree)

# ### Parcourir la liste et afficher pour chaque ligne les clés 'NOM' et 'CODE_POSTAL'
# for i in range(len(dicCSV)):
#     print(dicCSV[i]['NOM'], dicCSV[i]['CODE_POSTAL'])
# ### idem mais avec une autre méthode
# for var in dicCSV:
#     print(var['NOM'], var['CODE_POSTAL'])

# ### Autres manipulations ex :
# for i in range(len(dicCSV)):
     
#     print("<<< ligne n°", i, ">>>" )
#     print("Les items (\'clés\':\'valeurs\'):")                   # \ Pour annuler l'effet du caractere speciale '
#     print(dicCSV[i].items())
#     print("Seulement les clés:")
#     print(dicCSV[i].keys())
#     print("Seulement les valeurs converties en liste:")
#     print(list(dicCSV[i].values()))                             # Pour convertir le resultat en liste

