# Objectif du job :
# - Créer une classe Forme avec méthode aire retournant 0
# - Créer une classe Rectangle héritant de Forme
# - Surcharger la méthode aire pour calculer l'aire du rectangle
#
# Solution :
# - Classe de base simple
# - Héritage avec surcharge de méthode
# - Test du calcul d'aire

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__largeur * self.__hauteur

if __name__ == "__main__":
    rectangle = Rectangle(5, 3)
    print(f"L'aire du rectangle est: {rectangle.aire()}")
