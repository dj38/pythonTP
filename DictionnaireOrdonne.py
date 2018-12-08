class DictionnaireOrdonne:
    """
    Dictionnaire ordonne
    """


    def __init__(self,base={},**donnees):
        """
        Constructeur de l'objet
        :param base: un dictionnaire peut etre passe en argument
        :param donnees: une liste de couples clés, valeurs
        """
        self._cles=[]  # liste des clés
        self._valeurs=[]  # list des valeurs

        # cas ou un dict ou DictionnaireOrdonne est passé en argument
        if type(base) not in (dict,DictionnaireOrdonne):
            raise TypeError("une variable de type dict ou DictionnaireOrdonne doit etre passée au contructeur")
        for cle in base:
            self[cle]=base[cle]

        for cle in donnees:
            self[cle]=donnees[cle]

    def __repr__(self):
        """
        Methode utilisee lors d'une instruction print
        :return : string a afficher
        """
        myStr="{"
        premierPassage=True
        for (cle,valeur) in self.items():
            if not premierPassage:
                myStr += ", "
            myStr += "{}: {}".format(cle,valeur)
            premierPassage=False
        myStr+="}"
        return myStr

    def items(self):
        """
        renvoie un generateur comprenant les couples (clé,valeur)
        """
        for index,cle in enumerate(self._cles):
            yield (cle,self._valeurs[index])

    def keys(self):
        """
        generateur renvoyant les cles
        """
        for cle in self._cles:
            yield cle

    def values(self):
        """
        generateur renvoyant les valeurs
        """
        for valeur in self._valeurs:
            yield valeur

    def reverse(self):
        """
        Methode permettant d'inverser l'ordre de DictionnaireOrdonnee
        """
        self._cles.reverse()
        self._valeurs.reverse()

    def sort(self):
        """
        Method permettant de trier le DictionnaireInverse en fonction de ses cles
        """
        # On trie les clés
        cles_triees = sorted(self._cles)
        # On crée une liste de valeurs, encore vide
        valeurs = []
        # On parcourt ensuite la liste des clés triées
        for cle in cles_triees:
            valeur = self[cle]
            valeurs.append(valeur)
        # Enfin, on met à jour notre liste de clés et de valeurs
        self._cles = cles_triees
        self._valeurs = valeurs
    def __add__(self, other):
        """
        Methode permettant d'additioner 2 dictionnaires (les concatene)
        :param other: 2eme dictionnaire (a ajouter a self)
        """

    def __getitem__(self, cle):
        """
        Methode utilisee lors d'un acces a un element du dictionnaire
        :param item: clé
        """
        if cle not in self:
            raise KeyError("\"{}\" not in dictionary".format(cle))
        return  self._valeurs[self._cles.index(cle)]

    def __setitem__(self, cle, valeur):
        """
        Methode utilisee pour definir une nouvelle valeur
        """
        if cle in self:
            self._valeurs[self._cles.index(cle)]=valeur
        else:
            self._cles.append(cle)
            self._valeurs.append(valeur)

    def __delitem__(self, cle):
        """
        Methode permettant de supprimer l'element correspondant a la cle
        :param cle:
        """
        if cle in self:
            index=self._cles.index(cle)
            del self._cles[index]
            del self._valeurs[index]
        else:
            raise KeyError("\"{}\" not in dictionary".format(cle))

    def __contains__(self, cle):
        """
        Methode renvoie true si cle est present dans le dictionnaire. Appelee lors des commandes "in"
        :param cle:
        """
        return self._cles.__contains__(cle)

    def __len__(self):
        return len(self._cles)

if __name__=="__main__":
    myDict = {"pomme":5,"poire":2}
    fruits = DictionnaireOrdonne(myDict)
    print(fruits)
    fruits = DictionnaireOrdonne(pommes=15,poires=12)
    print(fruits)
    fruits.reverse()
    print(fruits)
    for cle in fruits.keys():
        print("cle : {}".format(cle))
    for valeur in fruits.values():
        print("valeur : {}".format(valeur))
    print("fruits[pommes] : {}".format(fruits["pommes"]))
    print("fruits[poires] : {}".format(fruits["poires"]))
    try:
        print("fruits[poire] : {}".format(fruits["poire"]))
    except:
        print("J'ai un souci avec poire")
    print("contains pommes {}".format("pommes" in fruits))
    print("contains pomme {}".format("pomme" in fruits))
    fruits["pommes"]=123
    print(fruits)
    fruits["cerises"]=52
    print(fruits)
    fruits.sort()
    print(fruits)
    del fruits["poires"]
    print(fruits)
    print("length : {}".format(len(fruits)))

