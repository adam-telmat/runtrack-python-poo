# Objectif du job :
# - Créer une classe Commande avec des attributs privés (numero, plats, statut)
# - Implémenter des méthodes pour gérer les commandes et les plats
# - Ajouter des calculs (total, TVA) et affichage
#
# Solution :
# - Création des attributs privés avec statut initialisé à "en cours"
# - Implémentation des méthodes de gestion des plats et du statut
# - Méthode privée pour les calculs (total, TVA)
# - Méthode d'affichage pour le résumé de la commande

class Commande:
    def __init__(self, numero_commande):
        self.__numero = numero_commande
        self.__plats = {}  
        self.__statut = "en cours"

    # Getters
    def get_numero(self):
        return self.__numero
    
    def get_statut(self):
        return self.__statut

    # Méthode privée
    def __calculer_total(self):
        return sum(plat["prix"] for plat in self.__plats.values())

    def ajouter_plat(self, nom, prix):
        self.__plats[nom] = {"prix": prix, "statut": "en cours"}

    def annuler_commande(self):
        self.__statut = "annulée"
        for plat in self.__plats.values():
            plat["statut"] = "annulé"

    def terminer_commande(self):
        self.__statut = "terminée"
        for plat in self.__plats.values():
            plat["statut"] = "terminé"

    def calculer_tva(self):
        return self.__calculer_total() * 0.20  # TVA à 20%

    def afficher_commande(self):
        print(f"Commande n°{self.__numero} - {self.__statut}")
        print("Plats commandés :")
        for nom, details in self.__plats.items():
            print(f"- {nom}: {details['prix']}€ ({details['statut']})")
        total = self.__calculer_total()
        tva = self.calculer_tva()
        print(f"Total HT: {total}€")
        print(f"TVA: {tva}€")
        print(f"Total TTC: {total + tva}€")



commande = Commande(1)

commande.ajouter_plat("Pizza", 12)
commande.ajouter_plat("Salade", 8)
commande.ajouter_plat("Tiramisu", 6)

print("État initial de la commande:")
commande.afficher_commande()

print("\nAprès avoir terminé la commande:")
commande.terminer_commande()
commande.afficher_commande()

print("\nNouvelle commande à annuler:")
commande2 = Commande(2)
commande2.ajouter_plat("Burger", 15)
commande2.annuler_commande()
commande2.afficher_commande()
