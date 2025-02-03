import math

# Job - Création de la classe Cercle
# 
# Objectif :
# - Créer une classe Cercle avec un attribut rayon initialisé dans le constructeur.
# - Ajouter les méthodes changerRayon(), afficherInfos(), circonference(), aire(), et diametre().
# - Créer deux cercles avec des rayons de 4 et 7, et afficher les informations, la circonférence, l'aire, et le diamètre de chaque cercle.
#
# Réponse :
# - La classe Cercle permet de gérer le rayon, de le modifier, d'afficher les informations et de calculer la circonférence, l'aire et le diamètre.
# - La méthode afficherInfos() affiche toutes les informations du cercle.
# - Les méthodes circonference(), aire() et diametre() retournent respectivement la circonférence, l'aire et le diamètre du cercle.

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Informations du Cercle 1 (Rayon 4) :")
cercle1.afficherInfos()
print("\nInformations du Cercle 2 (Rayon 7) :")
cercle2.afficherInfos()
