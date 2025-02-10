# Objectif du job :
# - Réutiliser la classe Forme du job04
# - Créer une classe Cercle héritant de Forme
# - Surcharger la méthode aire pour le cercle
# - Tester les deux surcharges (Rectangle et Cercle)
#
# Solution :
# - Réécriture des classes du job04
# - Nouvelle classe Cercle avec calcul d'aire
# - Tests comparatifs des deux formes

import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__largeur * self.__hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius
    
    def aire(self):
        return math.pi * self.__radius ** 2

if __name__ == "__main__":
    rectangle = Rectangle(5, 3)
    cercle = Cercle(4)

    print(f"L'aire du rectangle est: {rectangle.aire()}")
    print(f"L'aire du cercle est: {cercle.aire()}")
