class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        self.aire = 0
        self.peri = 0

    def périmètre(self):
        self.peri = (self.__largeur * 2) + (self.__longueur * 2)
        print(self.peri)

    def surface(self):
        self.aire = self.__longueur * self.__largeur
        print(self.aire)

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur = hauteur
        self.vol = 0

    def volume(self):
        self.vol = self.aire * self.hauteur
        print(self.vol)

test = Parallélépipède(2, 4, 2)
test.surface()
test.périmètre()
test.volume()
