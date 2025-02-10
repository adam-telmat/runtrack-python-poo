# Objectif du job :
# - Créer une classe Rectangle avec longueur et largeur en privé
# - Implémenter les méthodes perimetre et surface
# - Créer une classe Parallelepipede héritant de Rectangle
# - Ajouter le calcul du volume
#
# Solution :
# - Classes avec attributs privés
# - Méthodes de calcul simples
# - Héritage pour la 3D
# - Tests de toutes les méthodes

class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

if __name__ == "__main__":
    # Test Rectangle et toutes ses méthodes
    rectangle = Rectangle(5, 3)
    print("Test initial:")
    print(f"Rectangle de {rectangle.get_longueur()} x {rectangle.get_largeur()}")
    print(f"Périmètre: {rectangle.perimetre()}")
    print(f"Surface: {rectangle.surface()}")

    # Test des setters
    print("\nTest après modification:")
    rectangle.set_longueur(7)
    rectangle.set_largeur(4)
    print(f"Nouveau rectangle de {rectangle.get_longueur()} x {rectangle.get_largeur()}")
    print(f"Nouveau périmètre: {rectangle.perimetre()}")
    print(f"Nouvelle surface: {rectangle.surface()}")

    # Test Parallelepipede et toutes ses méthodes
    para = Parallelepipede(5, 3, 2)
    print("\nTest Parallélépipède:")
    print(f"Dimensions: {para.get_longueur()} x {para.get_largeur()} x {para.get_hauteur()}")
    print(f"Volume initial: {para.volume()}")
    
    # Test modification hauteur
    para.set_hauteur(4)
    print(f"Volume après modification hauteur: {para.volume()}")
