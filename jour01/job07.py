# Job 7 - Création de la classe Personnage
# 
# Objectif :
# - Créer une classe Personnage représentant un personnage de jeu.
# - Le plateau de jeu est représenté par une matrice.
# - Le joueur est défini par ses attributs x et y, représentant les index du tableau.
# - Créer le constructeur de la classe en initialisant la position (x et y).
# - Créer les méthodes : gauche, droite, bas et haut permettant respectivement
#   de faire avancer à gauche et à droite, en haut ou en bas.
# - Implémenter une méthode position() renvoyant les coordonnées sous forme d’un tuple.
#
# Réponse :
# - La classe Personnage a un constructeur qui initialise les attributs x et y pour définir la position du personnage sur la matrice.
# - Les méthodes gauche(), droite(), haut(), et bas() permettent de déplacer le personnage dans les directions correspondantes.
# - Chaque méthode modifie les coordonnées x et y en fonction de la direction choisie.
# - La méthode position() permet d'obtenir les coordonnées actuelles sous forme de tuple.

class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):   
        return (self.x, self.y)

personnage = Personnage(2, 3)

print(f"Position initiale : {personnage.position()}")

personnage.gauche()
print(f"Après déplacement à gauche : {personnage.position()}")

personnage.droite()
print(f"Après déplacement à droite : {personnage.position()}")

personnage.haut()
print(f"Après déplacement vers le haut : {personnage.position()}")

personnage.bas()
print(f"Après déplacement vers le bas : {personnage.position()}")

