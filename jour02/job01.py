# Objectif du job :
# - Créer une classe Rectangle avec des attributs privés (longueur et largeur)
# - Implémenter des accesseurs (getters) et mutateurs (setters) pour ces attributs
# - Tester la classe avec un rectangle de dimensions 10x5
# - Modifier les valeurs et vérifier les changements
#
# Solution :
# - Création d'une classe Rectangle avec longueur et largeur en privé
# - Implémentation des méthodes get_longueur() et get_largeur() pour accéder aux valeurs
# - Implémentation des méthodes set_longueur() et set_largeur() pour modifier les valeurs
# - Test avec un rectangle 10x5 puis modification des valeurs pour vérifier

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


rectangle = Rectangle(10, 5)

print(f"Longueur initiale : {rectangle.get_longueur()}")  
print(f"Largeur initiale : {rectangle.get_largeur()}")

rectangle.set_longueur(15)
rectangle.set_largeur(8)

print("\nAprès modification :")
print(f"Nouvelle longueur : {rectangle.get_longueur()}")
print(f"Nouvelle largeur : {rectangle.get_largeur()}")
