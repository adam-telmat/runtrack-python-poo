# Job 4 - Création de la classe Personne
#
# Objectif :
# - Créer une classe Personne avec les attributs nom et prenom.
# - Ajouter une méthode SePresenter() qui retourne une phrase avec le nom et le prénom.
# - Ajouter un constructeur permettant d'initialiser ces attributs.
# - Instancier plusieurs personnes et afficher leur présentation.
#
# Réponse :
# - La classe Personne est créée avec un constructeur qui initialise nom et prenom.
# - La méthode SePresenter() retourne une phrase sous la forme : "Je suis [prenom] [nom]".
# - On teste avec deux personnes pour vérifier que tout fonctionne correctement.

class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

print(personne1.SePresenter())
print(personne2.SePresenter())

