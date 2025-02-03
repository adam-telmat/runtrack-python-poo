# Job 2 - Affichage des attributs nombre1 et nombre2
# 
# Objectif :
# - À partir de la classe Operation créée précédemment, afficher en console 
#   la valeur des attributs nombre1 et nombre2.
#
# Réponse :
# - On instancie un objet de la classe Operation avec les valeurs 12 et 3.
# - Ensuite, on affiche les valeurs des attributs avec print().
# - Le résultat attendu est : 
#   "Le nombre1 est 12"
#   "Le nombre2 est 3"


class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation1 = Operation(12, 3)

print("Le nombre1 est", operation1.nombre1)
print("Le nombre2 est", operation1.nombre2)
