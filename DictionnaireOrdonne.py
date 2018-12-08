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
            self._cles.append(cle)
            self._valeurs.append(base[cle])

        for cle in donnees:
            self._cles.append(cle)
            self._valeurs.append(donnees[cle])

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
        


if __name__=="__main__":
    myDict = {"pomme":5,"poire":2}
    fruits = DictionnaireOrdonne(myDict)
    print(fruits)
    fruits = DictionnaireOrdonne(pommes=15,poires=12)
    print(fruits)
    fruits.reverse()
    print(fruits)
