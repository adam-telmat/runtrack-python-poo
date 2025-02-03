# Job 6 - Création de la classe Animal
# 
# Objectif :
# - Créer une classe Animal avec un attribut age initialisé à zéro et prenom initialisé à une chaîne vide dans son constructeur.
# - Instancier un objet Animal et afficher en console l'attribut age.
# - Créer une méthode vieillir() qui ajoute 1 à l'attribut age de l'animal.
# - Faire vieillir l'animal et afficher son âge mis à jour en console.
# - Créer une méthode nommer() qui prend en paramètre un nom et l'affiche.
#
# Réponse :
# - La classe Animal a été créée avec un constructeur qui initialise l'attribut age à 0 et prenom à une chaîne vide.
# - Un objet de la classe Animal a été instancié et son attribut age a été affiché avant et après l'appel à la méthode vieillir().
# - La méthode vieillir() ajoute 1 à l'âge de l'animal, et cet âge mis à jour est ensuite affiché.
# - La méthode nommer() permet de donner un nom à l'animal et de l'afficher en console.

class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}.")  

animal1 = Animal()

print(f"L'âge de l'animal {animal1.age} ans.")  

animal1.vieillir()

print(f"\033[90m#âge de l'animal après appel de la méthode vieillir\033[0m")
if animal1.age == 1:
    print(f"L'âge de l'animal {animal1.age} ans.") 
else:
    print(f"L'âge de l'animal {animal1.age} ans.") 

animal1.nommer("Luna")



