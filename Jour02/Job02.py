class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    def getTitre(self):
        return self.__titre
    def getAuteur(self):
        return self.__auteur
    def getPages(self):
        return self.__pages
    def setTitre(self, titre):
        self.__titre = titre
    def setAuteur(self, auteur):
        self.__auteur = auteur
    def setPages(self, pages):
        if pages >= 0:
            self.__pages = pages
        else:
            print("Le nombre de pages saisies n'existes pas")


onepiece = Livre("Harry Potter", "Oda", 192)


onepiece.setTitre("NN OP")
onepiece.setAuteur("Oda")
onepiece.setPages(1111)
print(onepiece.getTitre(), onepiece.getAuteur(), onepiece.getPages())
onepiece.setPages(0)
print(onepiece.getTitre(), onepiece.getAuteur(), onepiece.getPages())
onepiece.setPages(-22)
print(onepiece.getTitre(), onepiece.getAuteur(), onepiece.getPages())