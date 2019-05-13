# Exercice du dictionnaire ordonné - correction


import time



class DictionnaireOrdonne:
    """Création de la classe DictionnaireOrdonne"""
    
    def __init__(self, dicto={}, **donnees):                                    # instanciation
        """Constructeur de l'objet, instanciation de la classe."""
        
        self.cles = []                                                         # création d'une liste vide pour les clés
        self.valeurs = []                                                      # création d'une liste pour les valeurs
        
                                                                               # On vérifie que 'dicto' est de type dict()
        if type(dicto) not in (dict, DictionnaireOrdonne):
            raise TypeError("Attention, il doit s'agir d'un dictionnaire")
        
                                                                                # On récupère les données de 'dicto'
        for cle in dicto:
            self[cle] = dicto[cle]
        
                                                                                # On récupère les données de 'donnees'
        for cle in donnees:
            self[cle] = donnees[cle]
    


    def __repr__(self):
        """Représentation  de l'objet avec la méthode spéciale  'repr'"""
        
        chaine = "{"            # initialisation de la chaine 
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage: # condition permettant de placer la séparation
                chaine += ", " # On ajoute la virgule comme séparateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "}"
        return chaine
    
    def __str__(self):
        """méthode spéciale pour pouvoir utiliser print"""        
        return repr(self)
    
    def __len__(self):
        """Pour utiliser len, et connaitre la taille de l'élément"""
        return len(self.cles)
    
    def __contains__(self, cle):
        """Pour vérifier si la clé est dans la l'objet"""
        return cle in self.cles
    
    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe, lèveune exception KeyError sinon"""
        
        if cle not in self.cles:
            raise KeyError( f"La clé {cle} ne se trouve pas dans le dictionnaire")
        else:
            indice = self.cles.index(cle)
            return self.valeurs[indice]
    
    def __setitem__(self, cle, valeur):
        """Méthode spéciale appelée quand on cherche à modifier une clé
        présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
        à la fin du dictionnaire"""
        
        if cle in self.cles:
            indice = self.cles.index(cle)
            self.valeurs[indice] = valeur
        else:
            self.cles.append(cle)
            self.valeurs.append(valeur)
    
    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé"""
        if cle not in self.cles:
            raise KeyError( f"La clé {cle} ne se trouve pas dans le dictionnaire")
        else:
            indice = self.cles.index(cle)
            del self.cles[indice]
            del self.valeurs[indice]
    
    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self.cles)
    
    def __add__(self, autre_objet):
        """Retourne deux dictionnaires, self en premier et 'l'ajouté' en second """
        
        if type(autre_objet) is not type(self):
            raise TypeError(f"Impossible de concaténer {type.self} et {type(autre_objet)}")
        else:
            nouveau = DictionnaireOrdonne()
            
            # On commence par copier self dans le dictionnaire
            for cle, valeur in self.items():
                nouveau[cle] = valeur
            
            # On copie ensuite autre_objet
            for cle, valeur in autre_objet.items():
                nouveau[cle] = valeur
            return nouveau
    
    def items(self):
        """Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self.cles):
            valeur = self.valeurs[i]
            yield (cle, valeur)
    
    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self.cles)
    
    def values(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self.valeurs)
    
    def reverse(self):
        """Tri inversé"""
        cles = []
        valeurs = []
        for cle, valeur in self.items():
            # On ajoute les clés et valeurs au début de la liste
            cles.insert(0, cle)
            valeurs.insert(0, valeur)
        # On met ensuite à jour nos listes
        self.cles = cles
        self.valeurs = valeurs
    
    def sort(self):
        """Tri par clé"""
        # Tri des clés par ordre alphabétique
        cles_triees = sorted(self.cles)

        # On crée une liste de valeurs, encore vide
        valeurs = []

        # On parcourt ensuite la liste des clés triées
        for cle in cles_triees:
            valeur = self[cle]
            valeurs.append(valeur)
            
        # Enfin, on met à jour notre liste de clés et de valeurs
        self.cles = cles_triees
        self.valeurs = valeurs


def myprint(mess):
    time.sleep(1)
    print(f"\n{mess}\n")





        #################### TESTS DU DICTIONNAIRE ############################

myprint("### Création d'un dictionnaire vide :")
fruits = DictionnaireOrdonne()                                   # Instanciation d'un dictionnaire vide
myprint(f"Le dictionnaire fruits a été créé : {type(fruits)}")

fruits["pommes"] = 52
fruits["poires"] = 34
fruits["prunes"] = 128
fruits["melons"] = 15

myprint(fruits)                             

fruits["bananes"] = 21                                          # Ajout d'un élément clé/valeur dans le dictionnaire

myprint(fruits)

print(fruits["melons"])                                         # les indices sont couplés, melons retourne 15


del fruits["melons"]                                            
myprint("Suppression des clés 'melons/ et sa valeur' avec del, possible grace a la méthode delitem :")   # la méthode spéciale delitem permet de supprimer clé/valeur grace à del
myprint(fruits)

print(fruits)
print("items ci dessous :")
