#
# LISTE CHAINEE
#

#===================================================================================
# CLASS
#===================================================================================
class Cell:
    """Une cellule d'une liste chainee"""

    def __init__(self, v, s):
        self.value = v  # type pas precise
        self.next = s   # la prochaine cellule

class List:
    """Une liste chainee"""

    def __init__(self):
        self.head = None

    # Retourner True si la liste est vide
    def is_empty(self):
        return self.head is None

    # Ajouter une cellule à la fin de la liste
    def add_cell(self, v):
        self.head = Cell(v, self.head)
    
    # Renvoyer la longueur de la liste
    def length(self):
        return lst_length(self.head)

    # Renvoyer la nieme cellule de la liste
    def get_cell(self, n):
        """Renvoi le n ieme element d'une liste chainee, numerote a partir de 0"""
        return lst_get_cell(self.head, n)

    def reverse(self):
        self.head = lst_reverse(self.head)

    #  # Trier la liste
    # def sorted(self):
    #     self.head = lst_tri_select(self.head)

    # def switch(self, i, j):
    #     self.head = lst_exchange(self.head, i, j)

    # def insert(self, i, v):
    #     self.head = lst_insert(self.head, i, v)

    # def delete(self, i):
    #     self.head = lst_delete(self.head, i)

    


#===================================================================================
# Fonction sur pointeur de cellule (.head)
#===================================================================================
def lst_length(lsth):
    """Longeur d'une liste"""
    len = 0
    c = lsth
    # print("c=",c.next.value)
    while c is not None:
        c = c.next
        len += 1
    return len
