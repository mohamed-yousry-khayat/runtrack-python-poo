class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("x:", self.x, ", y:", self.y)

    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y


p1 = Point(5, 6)
p1.afficherLesPoints()

p1.afficherX()
p1.afficherY()

# changer les coordonnées
p1.changerX(25)
p1.changerY(30)
p1.afficherX()
p1.afficherY()