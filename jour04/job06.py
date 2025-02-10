# Objectif du job :
# - Créer une classe Vehicule avec marque, modèle, année, prix
# - Créer une classe Voiture (hérite de Vehicule) avec 4 portes
# - Créer une classe Moto (hérite de Vehicule) avec 2 roues
# - Ajouter la méthode demarrer avec message de base et surcharges
#
# Solution :
# - Classe parent avec attributs et méthode demarrer de base
# - Classes filles avec attributs spécifiques (portes/roues)
# - Surcharge des méthodes avec appel au parent (super)
# - Tests des informations et démarrages

class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.__marque}")
        print(f"Modèle: {self.__modele}")
        print(f"Année: {self.__annee}")
        print(f"Prix: {self.__prix}€")

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.__portes}")

    def demarrer(self):
        super().demarrer()  # Affiche "Attention, je roule"
        print("La voiture démarre vrooooom!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.__roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.__roues}")

    def demarrer(self):
        super().demarrer()  # Affiche "Attention, je roule"
        print("La moto démarre vroum vroum!")

if __name__ == "__main__":
    voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
    print("=== Informations Voiture ===")
    voiture.informationsVehicule()
    voiture.demarrer()

    print("\n=== Informations Moto ===")
    moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
    moto.informationsVehicule()
    moto.demarrer()
