# Job 5 - Création de la classe Point
#
# Objectif :
# - Créer une classe Point avec les attributs x et y (coordonnées).
# - Ajouter plusieurs méthodes :
#   - afficherLesPoints() : affiche les coordonnées du point.
#   - afficherX() et afficherY() : affichent respectivement x et y.
#   - changerX(nouvelle_valeur) et changerY(nouvelle_valeur) : modifient x et y.
# - Tester la classe avec un exemple d'utilisation.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"x = {self.x}")

    def afficherY(self):
        print(f"y = {self.y}")

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur

point1 = Point(7, 9)  
point1.afficherLesPoints()  

point1.changerX(14)  
point1.changerY(18)  

point1.afficherX()  
point1.afficherY()  
point1.afficherLesPoints()  
