#coding:utf-8


class Dictionnaire:
    """classe, destinée à produire des objets conteneurs, des dictionnaires ordonnés."""


    def __init__(self, param1="clé",param2 ="valeur" ):  # params sont optionnels, ils affichent "clé/valeur" par défaut dans le dico
        """Initialisation du dictionnaire"""
        self.param1 = param1
        self.param2 = param2
        self.dico = {param1:param2} # remplissage du dico initialisé avec les param prédéfinis


    def remplir(self, ajout):
        """Remplir le dictionnaire avec l'ajout spécifié"""
        self.ajout = ajout
        self.dico = dict(self.ajout)    #dict précise à python qu'il s'agit d'un dictionnaire


    def __str__(self):
        """méthode de classe permettant d'afficher le retour avec print() de facon lisible"""
        return f"dictionnaire  = {self.dico}"


    def __getitem__(self, cle): # méthode spéciale permettant de récupérer la valeur de l'indice dans le dictionnaire
        return self.dico[cle]









d1 = Dictionnaire()
print(d1)

ex = {"voiture": "clio", "avion" : "mirage"}

d1.remplir(ex)
print(d1["avion"])

