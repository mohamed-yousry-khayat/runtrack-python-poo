class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

animal = Animal()
print("L'animal a", animal.age, "ans")
animal.vieillir()
print("L'animal a", animal.age, "ans")

animal.nommer("Chat")
print("L'animal s'appelle", animal.prenom)