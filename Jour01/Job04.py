class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis", self.nom, self.prenom)


noms = [
    Personne("Khayat", "Yousry"),
    Personne("Megherfi", "Bachir"),
    Personne("Amri", "Miriam")
]

for personne in noms:
    personne.SePresenter()
