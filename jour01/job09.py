# Job - Création de la classe Produit
# 
# Objectif :
# - Créer une classe Produit avec les attributs nom, prixHT, TVA.
# - Implémenter une méthode CalculerPrixTTC() pour retourner le prix TTC du produit.
# - Ajouter une méthode afficher() qui liste l’ensemble des informations du produit.
# - Créer plusieurs produits et calculer leurs prix avec TVA.
# - Ajouter des méthodes permettant de modifier le nom du produit et son prix, et d’obtenir ces informations.
# - Modifier le nom et le prix de chaque produit et afficher le nouveau prix des produits.
#
# Réponse :
# - La classe Produit permet de gérer les informations des produits, notamment le nom, le prix hors taxe (HT), et la TVA.
# - La méthode `CalculerPrixTTC()` calcule le prix total incluant la TVA.
# - La méthode `afficher()` affiche toutes les informations du produit.
# - Des méthodes permettent de modifier les informations des produits et d'afficher les résultats modifiés.

class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom : {self.nom}, Prix HT : {self.prixHT}€, TVA : {self.TVA}%, Prix TTC : {self.CalculerPrixTTC()}€"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Produit A", 100, 20)  
produit2 = Produit("Produit B", 150, 5)   

print(produit1.afficher())
print(produit2.afficher())

produit1.modifierNom("Produit A Modifié")
produit1.modifierPrix(120)
produit2.modifierNom("Produit B Modifié")
produit2.modifierPrix(160)

print("\nAprès modification :")
print(produit1.afficher())
print(produit2.afficher())
