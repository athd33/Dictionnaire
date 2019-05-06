#coding:utf-8

import time

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


    def add_dic(self, dictionnaire):
        self.dictionnaire = dictionnaire
        self.dico.update(dictionnaire)   # utilisation de la fonction update pour ajouter le dictionnaire à la suite
        return self.dico



def myprint(message):
    time.sleep(1)
    print(message)










####################### TESTS DE LA CLASSE #######################################
myprint("Instanciation du dictionnaire 'd1'...")
d1 = Dictionnaire()  # instanciation du dictionnaire d1


myprint("affichage du dictionnaire instancié avec les valeurs par défaut : ")
myprint(f"dictionnaire d1: {d1}")           # la méthode __ini__ a créé un dictionnaire avec les valeurs renseignées par défaut


myprint("Création de deux dictionnaires : 'ex' et 'dicto' ")
ex = {"voiture": "clio", "avion" : "mirage", "commerce" : "bazard"} # création d'un premier dictionnaire
dicto = {"italie": "pizza", "inde": "riz", "france": "baguette" }   # création d'un second dictionnaire

myprint("Remplissage de d1 avec le dictionnaire 'ex'")
d1.remplir(ex)      #utilisation de la méthode remplir() destinée à remplir le dictionnaire instancié avec l'objet choisi dict() ici

myprint("Controle du remplissage avec l'utilisation de la méthode spéciale __repr__ :")
myprint(f"Dictionnaire d1 : {d1}")           #utilisation de la méthode spéciale __repr__ pour afficher l'objet de façon lisible avec print()

myprint("Suppression d'une clé/valeur avec la méthode spéciale __delitem__ ('commerce'): ")
del d1["commerce"]  #utilisation de la méthode __delitem__ qui permet d'effacer une clé avec sa valeur via la fonction del()

myprint("Vérification de l'effacement de 'commerce' avec del :")
print(d1)           # vérification de la destruction de "commerce" via del()

myprint("Modificaion de la valeur d'avion avec 'A380' au lieu de 'mirage' :")
d1["avion"] = "A380"    # ajout de clé / valeur
print(d1)               # vérification

myprint("Ajout de 'bateau' avec 'zodiac' :")
d1["bateau"] = "zodiac" # ajout de clé / valeur
print(d1)               # vérification

mot = "voitures"

myprint("Utilisation de la méthode spéciale __contains__ pour parcourir l'objet avec 'in' ")
if mot in d1:       #utlisation de la méthode spéciale __contains__ permet de parcourir pour vérifier si mot est dans d1 avec "in"
    print("Le mot est dedans")
else:
    print("Le mot ne figure pas dans le dictionnaire")


myprint("Dictionnaire trié avec la méthode utilisant la fonction 'sorted', ordre alphabétique : ")
d1.sort_function() # utilisation d'une méthode utilisant "sorted" pour afficher le dictionnaire trié par ordre alphabétique par clé [0]

myprint("Dictionnaire trié avec la méthode utilisant la fonction 'sorted', ordre alphabétique inversé avec Reverse=True : ")
d1.sort_revers_function() # utilisation d'une méthode de tri avec "sorted" et l'ajout de Reverse=True pour inverser l'ordre des résultats

myprint("Utilisation de la méthode keys() créée pour retourner les clés de l'objet : ")
d1.keys() # création d'une méthode keys() qui retourne les clés de l'objet

myprint("Utilisation de la méthode values() créée pour retourner les valeurs de l'objet : ")
d1.values() # création d'une méthode values() qui retourne les valeurs de l'objet

myprint("Utilisation de la méthode item() créée pour retourner les clés et valeurs de l'objet : ")
d1.item() # création de la fonction items qui retourne les clés et valeurs de l'objet

myprint("Utilisation de la méthode add_dic() pour ajouter un dictionnaire à l'objet : ")
d1.add_dic(dicto)  # création de la méthode add_dic() qui ajoute le dictionnaire à l'objet instancié

myprint("Le dictionnaire d1 contient 'ex' et 'dicto' :")
myprint(d1)