# Job 1 - Création de la classe Operation.
# 
# Objectif :
# - Créer une classe `Operation` avec un constructeur qui initialise deux attributs `nombre1` et `nombre2` à 0 par défaut.
# - Ensuite, instancier la classe et afficher l'objet.
#
# Réponse :
# - La classe `Operation` a été créée avec un constructeur qui initialise les attributs `nombre1` et `nombre2` à 0 par défaut.
# - L'objet `operation1` a été instancié sans valeurs, ce qui utilise les valeurs par défaut (0).
# - L'affichage de l'objet avec `print(operation1)` montre l'adresse mémoire de l'objet.

class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation1 = Operation()

print(operation1)

