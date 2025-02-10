# Objectif du job :
# - Créer un jeu de Blackjack
# - Implémenter les règles de base (21 points max)
# - Gérer les valeurs des cartes (2-10, figures, as)
# - Créer le système de tour par tour
#
# Solution :
# - Classe Carte pour représenter chaque carte
# - Classe Jeu pour gérer la partie
# - Méthodes pour distribuer et jouer
# - Interface simple en console

import random

class Carte:
    def __init__(self, valeur, couleur):
        self.__valeur = valeur
        self.__couleur = couleur

    def get_valeur(self):
        if self.__valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.__valeur == 'As':
            return 11  
        return self.__valeur

    def __str__(self):
        return f"{self.__valeur} de {self.__couleur}"

class Jeu:
    def __init__(self):
        self.__paquet = []
        self.__initialiser_paquet()
        self.__main_joueur = []
        self.__main_croupier = []

    def __initialiser_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                self.__paquet.append(Carte(valeur, couleur))
        random.shuffle(self.__paquet)

    def __calculer_points(self, main):
        points = 0
        as_count = 0
        for carte in main:
            if carte.get_valeur() == 11:  # C'est un As
                as_count += 1
            points += carte.get_valeur()
        
        while points > 21 and as_count > 0:
            points -= 10
            as_count -= 1
        return points

    def distribuer_cartes_initiales(self):
        self.__main_joueur = [self.__paquet.pop(), self.__paquet.pop()]
        self.__main_croupier = [self.__paquet.pop(), self.__paquet.pop()]

    def afficher_mains(self, montrer_croupier=False):
        print("\nVotre main:")
        for carte in self.__main_joueur:
            print(f"- {carte}")
        print(f"Total: {self.__calculer_points(self.__main_joueur)}")

        print("\nMain du croupier:")
        if montrer_croupier:
            for carte in self.__main_croupier:
                print(f"- {carte}")
            print(f"Total: {self.__calculer_points(self.__main_croupier)}")
        else:
            print(f"- {self.__main_croupier[0]}")
            print("- [Carte cachée]")

    def joueur_tire_carte(self):
        self.__main_joueur.append(self.__paquet.pop())
        return self.__calculer_points(self.__main_joueur) <= 21

    def croupier_joue(self):
        while self.__calculer_points(self.__main_croupier) < 17:
            self.__main_croupier.append(self.__paquet.pop())

    def determiner_gagnant(self):
        points_joueur = self.__calculer_points(self.__main_joueur)
        points_croupier = self.__calculer_points(self.__main_croupier)

        if points_joueur > 21:
            return "Perdu ! Vous avez dépassé 21."
        elif points_croupier > 21:
            return "Gagné ! Le croupier a dépassé 21."
        elif points_joueur > points_croupier:
            return "Gagné ! Vous avez plus de points que le croupier."
        elif points_joueur < points_croupier:
            return "Perdu ! Le croupier a plus de points."
        else:
            return "Égalité !"

if __name__ == "__main__":
    jeu = Jeu()
    jeu.distribuer_cartes_initiales()
    
    # Tour du joueur
    perdu = False
    while True:
        jeu.afficher_mains()
        choix = input("\nVoulez-vous tirer une carte ? (o/n): ")
        if choix.lower() != 'o':
            break
        if not jeu.joueur_tire_carte():
            print("Vous avez dépassé 21 !")
            perdu = True
            break

    # Tour du croupier seulement si le joueur n'a pas perdu
    if not perdu:
        print("\nTour du croupier:")
        jeu.croupier_joue()
    
    # Résultat final
    print("\n=== Résultat final ===")
    jeu.afficher_mains(True)
    print("\n" + jeu.determiner_gagnant())
