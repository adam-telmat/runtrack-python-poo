# Objectif du job :
# - Créer une classe Rectangle avec des attributs privés (longueur, largeur)
# - Implémenter des accesseurs et mutateurs pour ces attributs
# - Tester la classe avec un rectangle de dimensions spécifiques
# - Modifier les valeurs et vérifier les changements
#
# Solution :
# - Création d'une classe Rectangle avec longueur et largeur en privé
# - Implémentation des méthodes get_longueur() et get_largeur() pour accéder aux valeurs
# - Implémentation des méthodes set_longueur() et set_largeur() pour modifier les valeurs
# - Test avec un rectangle puis modification des valeurs pour vérification

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Getters
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Setters
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
