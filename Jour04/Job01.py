class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, int):
        self.age = int
        print(self.age)


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai" + self.age + " " + " ans")


class Professeur(Personne):

    def __init__(self, matiere):
        self.__matiereEnseigné = matiere

    def enseigner(self):
        print("Le cours va commencer")

    def testu(self):
        return self.__matiereEnseigné

age = Personne()
age.afficherAge()
age.modifierAge(34)