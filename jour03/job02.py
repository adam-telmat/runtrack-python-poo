# Objectif du job :
# - Créer une classe CompteBancaire avec attributs privés (numero_de_compte, nom, prenom, solde)
# - Implémenter les méthodes de gestion (afficher, afficherSolde, versement, retrait)
# - Ajouter la gestion du découvert et des agios
# - Permettre les virements entre comptes
#
# Solution :
# - Création de la classe avec attributs privés
# - Implémentation des méthodes de gestion du compte
# - Tests avec deux comptes (un normal, un à découvert)

class CompteBancaire:
    def __init__(self, numero_de_compte, nom, prenom, solde, decouvert=False):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self.__numero_de_compte}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Solde: {self.__solde}€")

    def afficherSolde(self):
        print(f"Solde: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué")
            self.afficherSolde()
        else:
            print("Solde insuffisant")

    def agios(self):
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.05
            self.__solde -= agios
            print(f"Application d'agios: -{agios}€")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            print(f"Virement de {montant}€ effectué")
            self.afficherSolde()
        else:
            print("Solde insuffisant pour le virement")

# Tests
compte1 = CompteBancaire("1234", "Doe", "John", 1000)
compte2 = CompteBancaire("5678", "Martin", "Sophie", -500, True)

print("État initial des comptes:")
compte1.afficher()
print()
compte2.afficher()

print("\nVirement pour rembourser le découvert:")
compte1.virement(compte2, 500)

print("\nÉtat final des comptes:")
compte1.afficher()
print()
compte2.afficher()
