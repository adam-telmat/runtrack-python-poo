# Job 3 - Ajout d'une méthode addition()
# 
# Objectif :
# - Modifier la classe Operation pour y ajouter une méthode addition().
# - Cette méthode doit additionner nombre1 et nombre2, puis afficher le résultat.
#
# Réponse :
# - On ajoute une méthode addition() qui effectue nombre1 + nombre2 et l'affiche.
# - Ensuite, on instancie un objet avec les valeurs 12 et 3.
# - On appelle addition() pour voir le résultat.
# - Le résultat attendu est : 
#   "Le résultat de l'addition est : 15"

class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", resultat)

operation1 = Operation(12, 3)

operation1.addition()
