class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print(self.marque, self.modèle, self.année, self.prix)


class Voiture(Vehicule):
   def __init__(self):
        Vehicule.informationsVehicule()
        self.portes = 4

    def informationsVehicule(self):
        print(self.marque, self.modèle, self.année, self.prix, self.portes)

test = Voiture("BMW", "X9", "2034", "2034")
test.informationsVehicule()