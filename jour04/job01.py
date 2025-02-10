# Objectif du job :
# - Créer une classe Personne avec age=14 par défaut
# - Créer les méthodes afficherAge, bonjour, modifierAge
# - Créer une classe Eleve qui hérite de Personne
# - Créer une classe Professeur avec attribut matiereEnseignee
#
# Solution :
# - Implémentation des trois classes avec héritage
# - Méthodes de base dans Personne
# - Méthodes spécifiques dans Eleve et Professeur
# - Tests de vérification des fonctionnalités

class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiere):
        super().__init__()
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")

if __name__ == "__main__":
    print("=== Test de la classe Personne ===")
    personne = Personne()
    personne.bonjour()
    personne.afficherAge()
    personne.modifierAge(33)
    print("Après modification:")
    personne.afficherAge()

    print("\n=== Test de la classe Eleve ===")
    eleve = Eleve()
    print("Âge de l'élève par défaut:", end=" ")
    eleve.afficherAge()
    eleve.bonjour()
    eleve.allerEnCours()

    print("\n=== Test de la classe Professeur ===")
    prof = Professeur("Mathématiques")
    prof.bonjour()
    prof.enseigner()
