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


    def __repr__(self):
        """méthode de classe permettant d'afficher le retour avec print() de facon lisible"""
        return f"{self.dico}"


    def __getitem__(self, cle): # méthode spéciale permettant de récupérer la valeur de l'indice dans le dictionnaire
        return self.dico[cle]


    def __setitem__(self, key, value):  # méthode permettant de modifier la valeur d'une clé
        self.dico[key] = value
        return self.dico[key]


    def __delitem__(self, key): # méthode permettant d'utiliser del pour effacer un élément par sa clé
        del self.dico[key]


    def __contains__(self, item): # permet de vérifier la présence de item dans le dictionnaire
        return item in self.dico.keys()


    def __len__(self):          # permet de récupérer la longeur avec la fonction len()
        return len(self.dico)


    def __str__(self):
        return f"{self.dico}"

    def sort_function(self):                                    #fonction pour afficher la liste triée par clé
        print(sorted(self.dico.items(), key=lambda t:t[0]))     # correspond à l'incice de l'objet à utiliser pour référence du tri


    def sort_revers_function(self):                             # fonction pour affichier la liste triée inversée
        print((sorted(self.dico.items(), key=lambda t:t[0], reverse=True)))


    def item(self):         # fonction qui retourne les clés et valeurs de l'objet
        d = self.dico
        for cle, valeur in d.items():
            print(f"{cle}:{valeur}")


    def keys(self):         # fonction qui retourne uniquement les clés de l'objet
        d = self.dico
        for cle in d.keys():
            print(cle)

    def values(self):       # fonction qui retourne uniquement les valeurs de l'objet
        d = self.dico
        for value in d.values():
            print(value)







d1 = Dictionnaire()
print(d1)

ex = {"voiture": "clio", "avion" : "mirage", "bazard" : "bordel"}
d1.remplir(ex)
print(d1)
del d1["bazard"]                #del possible grace à __delitem__
print(d1)
d1["avion"] = "A380"
print(d1)

d1["bateau"] = "zodiac"
print(d1)

mot = "voitures"

if mot in d1:       #methode spéciale __contains__ permet de parcourir pour vérifier si mot est dans d1
    print("Le mot est dedans")
else:
    print("Le mot ne figure pas dans le dictionnaire")

print(d1)

d1.sort_function()
d1.sort_revers_function()
d1.keys()
d1.values()
d1.item()