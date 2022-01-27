#!/usr/bin/python3
#
# @File : gd_ouvrir_fichier.py
#
# @Authors : Guillaume DAGUET
#            gd.guillaume.daguet@gmail.com
#            [+|]
#
# @Date : 01/10/2021
#
# @Version : V1.1.0
#
# @Synopsis : 
#       
#       Ouverture d'un fichier en lecture : open(fichier, "r")
#           => Méthodes read(), readline() et readlines()
#       Ouverture d'un fichier en écriture : open(fichier, "w") ou open(fichier, "a")
#           => Méthode write()
#
#       r, pour une ouverture en lecture (READ).
#       w, pour une ouverture en écriture (WRITE), à chaque ouverture le contenu du fichier est écrasé. Si le fichier n'existe pas python le crée.
#       a, pour une ouverture en mode ajout à la fin du fichier (APPEND). Si le fichier n'existe pas python le crée.
#
#
#  < N° DE VERSION >
#
#   w.x.y : 
#
#    + w est le numéro de version Majeure : 
#       il est incrémenté lorsque de grosses modifications ont été apportées, et qui cassent la compatibilité avec la version majeure précédente w-1,
#       nécessitant donc de grosses modifications dans les projets pour la migration.
#
#    + x est le numéro de version Mineure : 
#       il est incrémenté quand il y a de nouvelles fonctionnalités, évolutions, corrections de bugs etc. 
#       Par contre un projet basé sur une version w.x doit être # compatible avec une version w.x-1.
#
#    + y est le numéro de version de correction, appelé Release: il change quand il y a eu simplement des corrections de bugs par rapport à la version w.x.y-1.
#
#
# =============================================================================
# IMPORTATION DES LIBRAIRIES
# =============================================================================

import datetime                                                 # Module de fonction pour la date

# =============================================================================
# DECLARATION DES VARIABLES GLOBALES
# =============================================================================

### Recuperer la date courante
dateISOFormat = datetime.datetime.now()
date = dateISOFormat.isoformat("-", "minutes")

### Configuration
repEntree = "workspace/database"                                # Chemin du repertoire d'entree
repSortie = "workspace/tmp"                                     # Chemin du repertoire de sortie

#nom_fichier = 'agile.txt'
nom_fichier = 'villes_guadeloupe.csv'

fichEntree = repEntree + '/' + nom_fichier # Chemin complet vers le fichier d'entree ('+' = concatenation de chaine)
fichSortie = repSortie + '/' + nom_fichier + '.' + date # Chemin complet vers le fichier de sortie

# =============================================================================
# DECLARATION DES FONCTIONS
# =============================================================================

# -------------------------------------
# [[ Ouvrir un fichier en lecture ]]
# -------------------------------------

### Methode 1 avec read : Fichier ==> chaine de caractere (string)
def ouvir_fichier_read(fichier):
    """
    Ouvir fichier et stocker tout son contenu dans une chaine de caractere.
    Méthode classique d'ouverture de fichier.
    """

    filin = open(fichier, 'r')                                  # Ouvrir le fichier en lecture, filin est un descripteur de fichier (filin pour les fichier d'entrée)
    strFichier = filin.read()                                   # Appel la méthode read() de l'objet filin pour stocker le contenu du fichier dans la variable strFichier
    filin.close()                                               # Fermeture du fichier  
 
    return strFichier                                           # Retourne la variable de type chaine de caratere (string) contenant la totalité du fichier

### Methode 1bis (ouverture spécifique python) avec read :  Fichier ==> chaine de caractere (string)
def ouvir_fichier_read_bis(fichier):
    """
    Ouvir fichier et stocker tout son contenu dans une chaine de caractere.
    Methode "with open" pour ouvrir le fichier. Pas besoin de le clore avec filin.close().
    """

    with open(fichier, "r") as filin:                           # Methode alternative d'ouverture du fichier (pas besoin de clore le fichier)
        strFichier = filin.read()                               # Appel la méthode read() de l'objet filin  

    return strFichier                                           # Retourne la variable de type chaine de caratere (string) contenant la totalité du fichier

### Methode 2 avec readline : Fichier ==> Ligne par ligne du ficher dans une chaine de caratere
def ouvir_fichier_readline(fichier):
    """
    Ouvir le fichier, le parcourir ligne par ligne et stocker le contenu de la ligne courante dans une chaine de caractere
    """

    with open(fichier, "r") as filin:                           # Ouvrir le fichier en lecture, filin est un descripteur de fichier (filin pour les fichier d'entrée)
        
        strLigne = filin.readline().rstrip()                    # La méthode readline() lis une ligne du fichier, la stocke dans une chaine de caractere et fait pointer filin sur la ligne suivante 
            
        while strLigne != "":                                   # Boucler tant que filin n'a pas atteind la fin du fichier (dans ce cas strLigne == "")
            
            # <<Fonction de TRAITEMENT A FAIRE à chaque itération :
            # ex: stocker strLigne dans un tableau comme dans ouvir_fichier_readline_tab
            #     ou faire un traitement sur strLigne (remplacer un caractere) 
            #     puis stocker le résultat dans un fichier...>>

            strLigne = filin.readline().rstrip()                # Recuperer la ligne courante du ficher et on la stock dans strLigne

    # return foo                                                # Suivant le traitement on mettra ou non un return 

### Ex. de Methode 2 avec readline : Fichier ==> chaque ligne du ficher dans une colonne de tableau (liste)
def ouvir_fichier_readline_tab(fichier):
    """
    Ouvir fichier, le parcourir ligne par ligne et stocker ajouter la ligne courante a la fin tableau
    """
    
    with open(fichier, "r") as filin:                           # Ouvrir le fichier en lecture, filin est un descripteur de fichier (filin pour les fichier d'entrée)

        lstFichier=[]                                           # Initialisation du tableau qui va servir à stocker les lignes du fichier
        strLigne = filin.readline().rstrip()                    # La méthode readline() lis une ligne du fichier, la stocke dans une chaine de caractere et fait pointer filin sur la ligne suivante 

        while strLigne != "":                                   # Boucler tant que filin n'a pas atteind la fin du fichier (dans ce cas strLigne == "")

            # <<TRAITEMENT A FAIRE (à chaque itération)>>
            lstFichier.append(strLigne)                         # Ajouter avec append la ligne courante à la fin du tableau
    
            strLigne = filin.readline().rstrip()                # Recuperer la ligne courante du ficher et on la stack dans strLigne

    return lstFichier                                           # Retourner lstFichier, un tableau de chaine de caractere contenant toute les lignes du fichier


### Methode 3 avec readlines : Fichier ==> chaque ligne du ficher dans une colonne de tableau (liste)
def ouvir_fichier_readlines(fichier):
    """
    Ouvrir le fichier et placer directement chaque ligne du fichier dans une case de tableau
    """

    with open(fichEntree, 'r') as filin:                        # Ouvrir le fichier en lecture, filin est un descripteur de fichier (filin pour les fichier d'entrée)
        strFichier = filin.readlines()                          # La methode readlines place directement chaque ligne du fichier dans une case de tableau (pas besoin d'inialiser le tableau)

    return strFichier

# -------------------------------------
# [[ Ouvrir un fichier en écriture ]]
# -------------------------------------

### Méthode 4 : Ecrire avec la méthode write
def ouvir_fichier_write(fichier):                               # Ouvrir le fichier en écriture, filout est un descripteur de fichier (filout pour les fichier de sortie)
    """
    Ouvir le fichier en écriture et ajouter du texte dedans
    """

    with open(fichier, "w") as filout:                          # On pourra mettre également "a"
        filout.write("Hello World!")                            # Appeler la méthode write() de l'objet filout : ecrire "Hello World!" dans le fichier


##############################################################################
# MAIN : Partie principal du programme
##############################################################################
""" 
C'est ici que se trouve la partie principale du code. Dans cette partie on va, 
suivant notre besoin, appeller toutes les fonctions et variables déclarées ci-dessus.
"""

### READ() 
print("\nMethode 1 avec read : Fichier ==> chaine de caractere :\n")
fichier_string = ouvir_fichier_read(fichEntree)
print(fichier_string)
print("type de la variable :", type(fichier_string))

### READLINE
print("\nMethode 2bis avec readline :\n")
fichier_liste = ouvir_fichier_readline_tab(fichEntree)
print(fichier_liste)
print("type de la variable :", type(fichier_liste))

### READLINES
print("\nMethode 3 avec readlines :\n")
fichier_liste2 = ouvir_fichier_readlines(fichEntree)
print(fichier_liste2)
print("type de la variable :", type(fichier_liste2))

#print(ouvir_fichier_read_bis.doc)

### WRITE
print("\nMethode 4 avec write :\n")
ouvir_fichier_write(fichSortie)
print("Ouvrez : ", fichSortie )
