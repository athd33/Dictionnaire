#coding:utf-8


class Dictionnaire:
    """classe, destinée à produire des objets conteneurs, des dictionnaires ordonnés."""
    def __init__(self):
        self.dicto = {}


    def __str__(self):
        """méthode de classe permettant d'afficher le retour avec print() de facon lisible"""
        return self.dicto


#################### EN COURS #####################################