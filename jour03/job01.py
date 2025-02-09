# Objectif du job :
# - Créer une classe Ville avec nom et nombre d'habitants en privé
# - Créer une classe Personne liée à une ville
# - Implémenter une méthode pour augmenter la population
#
# Solution :
# - Création des classes avec attributs privés
# - Méthode ajouterPopulation qui incrémente les habitants
# - Tests avec Paris et Marseille

class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nb_habitants(self):
        return self.__nb_habitants

    def ajouter_habitant(self):
        self.__nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajouter_habitant()

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris: {paris.get_nb_habitants()} habitants")
print(f"Population de la ville de Marseille: {marseille.get_nb_habitants()} habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Mise a jour de la population de la ville de Paris: {paris.get_nb_habitants()} habitants")
print(f"Mise a jour de la population de la ville de Marseille: {marseille.get_nb_habitants()} habitants")
