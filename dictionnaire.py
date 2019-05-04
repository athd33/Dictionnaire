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


    def __setitem__(self, key, value):  # méthode permettant de modifier la valeur d'une clé
        self.dico[key] = value
        return self.dico[key]

    def __delitem__(self, key): # méthode permettant d'utiliser del pour effacer un élément par sa clé
        del self.dico[key]

    def __contains__(self, item): # permet de vérifier la présence de item dans le dictionnaire
        return item in self.dico.keys()




d1 = Dictionnaire()
print(d1)

ex = {"voiture": "clio", "avion" : "mirage", "bazard" : "bordel"}
d1.remplir(ex)
print(d1)
del d1["bazard"]
print(d1)
d1["avion"] = "A380"
print(d1)

d1["bateau"] = "zodiac"
print(d1)

mot = "voitures"
if mot in d1:
    print("Le mot est dedans")
else:
    print("Le mot ne figure pas dans le dictionnaire")
