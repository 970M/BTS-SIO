import fa_list_lib

# Initialiser une liste
maListe = fa_list_lib.List()

# Afficher si elle est vide
print("Ma liste est vide?",maListe.is_empty())

maListe.add_cell("TOTO")
maListe.add_cell(0)

# Afficher si elle est vide
print("Ma liste est vide?",maListe.is_empty())

# Afficher la longueur de la liste
print("Voici sa longueur:",maListe.length())


### Partie à décommenter lorsque les fonctions seront opérationnelles

# # Afficher le n eme élément de la liste (! commence à  0)
# print("Voici le 3 eme élément ",maListe.get_cell(2))
# # Parcourir toute la liste
# for j in range(1, maListe.length()):
#     print("Element n°", j, ':', maListe.get_cell(j))

# # Renverser l liste
# maListe.reverse()
