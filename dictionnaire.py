class DictionnaireOrdonne:
    """Dictionnaire ordonné"""
    
    def __init__(self, base={}, **donnees):             ###### 1er POINT #####
        """
        Méthode d'instanciation du Dictionnaire:
        base={} créé un dictionnaire par défaut, si rien n'est renseigné en paramètre,
        (**donnees) entre des paramètres sous forme de dictionnaire avec ** """
        
        self.cles = [] # Liste contenant nos clés
        self.valeurs = [] # Liste contenant les valeurs correspondant à nos clés
        
        # On vérifie que 'base' est un dictionnaire exploitable
        if type(base) not in (dict, DictionnaireOrdonne):
            raise TypeError( \
                "le type attendu est un dictionnaire (usuel ou ordonne)")
        
        # On récupère les données de 'base'
        for cle in base:
            self[cle] = base[cle]
        
        # On récupère les données de 'donnees'
        for cle in donnees:
            self[cle] = donnees[cle]
    

    def __repr__(self):                                 ###### 2eme POINT  ######
        """Représentation de notre objet. C'est cette chaîne qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en
        utilisant la fonction 'repr'"""
        
        chaine = "{"
        premier_passage = True
        for cle, valeur in self.items():
            if not premier_passage:
                chaine += ", " # On ajoute la virgule comme séparateur
            else:
                premier_passage = False
            chaine += repr(cle) + ": " + repr(valeur)
        chaine += "}"
        return chaine
    
    def __str__(self):
        """Méthode spéciale pour pouvoir utiliser 'print' """
        return repr(self)
    
    def __len__(self):
        """Renvoie la taille du dictionnaire"""
        return len(self.cles)
    
    def __contains__(self, cle):
        """Permet de rechercher la clé dans le dictionnaire avec 'in'"""
        return cle in self.cles
    
    def __getitem__(self, cle):
        """Renvoie la valeur correspondant à la clé si elle existe, lève
        une exception KeyError sinon"""
        
        if cle not in self.cles:
            raise KeyError(f"La clé {cle} ne se trouve pas dans le dictionnaire")
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
            raise KeyError( \
                "La clé {0} ne se trouve pas dans le dictionnaire".format( \
                cle))
        else:
            indice = self.cles.index(cle)
            del self.cles[indice]
            del self.valeurs[indice]
    
    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self.cles)
    
    def __add__(self, autre_objet):
        """Dictionnaires mis bout à bout (d'abord self puis autre_objet)"""
        
        if type(autre_objet) is not type(self):
            raise TypeError( \
                "Impossible de concaténer {0} et {1}".format( \
                type(self), type(autre_objet)))
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
        """Renvoie les couples (cle, valeur)"""
        for i, cle in enumerate(self.cles):
            valeur = self.valeurs[i]
            yield (cle, valeur)
    
    def keys(self):
        """Renvoie les clés"""
        return list(self.cles)
    
    def values(self):
        """Renvoir la liste des valeurs"""
        return list(self.valeurs)
    
    def reverse(self):
        """Inversion du dictionnaire"""
        # Création de deux listes pour ordonner le nouveau dictionnaire
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
        """Sort pour trier le dictionnaire par clés"""
        # On trie les clés
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
    print(f"{mess}\n")





####### TESTS ####################

####### 1er POINT #######
myprint("instanciation de fruits avec la méthode __init__() :")

fruits = DictionnaireOrdonne()

myprint("Ajouts de clés / valeurs dans le dictionnaire : ")

fruits["pommes"] = 44
fruits["poires"] = 21
fruits["prunes"] = 221
fruits["melons"] = 93

print(f"\nAffichage du dictionnaire avec print : {fruits}:")

# modifications possibles

fruits["pommes"] = "00, plus de pommes"
myprint(f"\nModification de la valeur de la clé 'pommes' {fruits}:")


                            # in permis par la méthode contains
if "bananes" in fruits:
    print("Il y a des bananes")
else:
    print("Pas de bananes")

print(f"\nLa longueur du dictionnaire est de {len(fruits)} clés")


                    # parcours du dictionnaire par clé
for cle in fruits:
    print(cle)

                                                            # renvoie les clés
print(f"\n Affichage des clés avec keys() : {fruits.keys()}")

                                                            # renvoie les valeurs
print(f"\n Affichage des valeurs avec values() : {fruits.values()}")

