# Objectif du job :
# - Créer un jeu de combat tour par tour avec niveaux de difficulté
# - Créer une classe Personnage (nom, points de vie, attaque)
# - Créer une classe Jeu (choix niveau, gestion combat)
# - Gérer les combats avec des dégâts aléatoires
# - Gérer les erreurs de saisie utilisateur
#
# Solution :
# - Classe Personnage avec attributs privés et dégâts aléatoires (5-15)
# - Classe Jeu avec 3 niveaux de difficulté :
#   * Facile   : Joueur (120 PV) vs Gobelin (60 PV)
#   * Normal   : Joueur (100 PV) vs Chevalier (100 PV)
#   * Difficile: Joueur (80 PV) vs Dragon (140 PV)
# - Combat interactif tour par tour avec affichage des points de vie

class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie
        self.__vie_max = vie  

    def get_nom(self):
        return self.__nom

    def get_vie(self):
        return self.__vie

    def attaquer(self, cible):
        from random import randint
        degats = randint(5, 15)
        cible.__vie -= degats
        if cible.__vie < 0:  
            cible.__vie = 0
        print(f"{self.__nom} attaque {cible.__nom} et lui inflige {degats} points de dégâts")
        print(f"Il reste {cible.__vie}/{cible.__vie_max} points de vie à {cible.__nom}")

class Jeu:
    def __init__(self):
        self.__niveau = 0
        self.__joueur = None
        self.__ennemi = None

    def choisirNiveau(self):
        while True:  
            print("\nChoisissez le niveau de difficulté:")
            print("1. Facile (Ennemi faible)")
            print("2. Normal (Ennemi équilibré)")
            print("3. Difficile (Ennemi puissant)")
            try:
                choix = int(input("Votre choix (1-3): "))
                if 1 <= choix <= 3:
                    self.__niveau = choix
                    break
                print("Veuillez choisir 1, 2 ou 3")
            except ValueError:
                print("Veuillez entrer un nombre")

    def lancerJeu(self):
        vies = {
            1: (120, 60),    
            2: (100, 100),   
            3: (80, 140)     
        }
        vie_joueur, vie_ennemi = vies[self.__niveau]
        
        noms_boss = {
            1: "Gobelin",
            2: "Chevalier Noir",
            3: "Dragon"
        }
        
        self.__joueur = Personnage("John", vie_joueur)
        self.__ennemi = Personnage(noms_boss[self.__niveau], vie_ennemi)
        
        print(f"\nVous affrontez {self.__ennemi.get_nom()} !")
        self.combat()

    def verifierSante(self, personnage):
        return personnage.get_vie() > 0

    def verifierGagnant(self):
        if not self.verifierSante(self.__ennemi):
            print(f"\nFélicitations! {self.__joueur.get_nom()} a gagné!")
            return True
        elif not self.verifierSante(self.__joueur):
            print(f"\nGame Over! {self.__ennemi.get_nom()} a gagné!")
            return True
        return False

    def combat(self):
        tour = 1
        while True:
            print(f"\n=== Tour {tour} ===")
            print(f"\nVos points de vie: {self.__joueur.get_vie()}")
            print(f"Points de vie de l'ennemi: {self.__ennemi.get_vie()}")
            input("\nAppuyez sur Entrée pour attaquer...")
            
            self.__joueur.attaquer(self.__ennemi)
            if self.verifierGagnant():
                break
            
            print("\nL'ennemi se prépare à attaquer !")
            input("Appuyez sur Entrée pour continuer...")
                
            self.__ennemi.attaquer(self.__joueur)
            if self.verifierGagnant():
                break
                
            tour += 1

# Test du jeu
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
