# Objectif du job :
# - Créer une classe Joueur (nom, numéro, position, buts, passes, cartons)
# - Créer une classe Equipe (nom, liste de joueurs)
# - Ajouter les méthodes de gestion (marquer, passe, cartons)
# - Ajouter les méthodes d'affichage et mise à jour
#
# Solution :
# - Classes avec attributs privés
# - Méthodes simples pour chaque action
# - Tests avec France vs Brésil

class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0

    def marquerUnBut(self):
        self.__buts += 1
        print(f"{self.__nom} a marqué un but!")

    def effectuerUnePasseDecisive(self):
        self.__passes += 1
        print(f"{self.__nom} fait une passe décisive!")

    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1
        print(f"{self.__nom} reçoit un carton jaune")

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1
        print(f"{self.__nom} reçoit un carton rouge!")

    def afficherStatistiques(self):
        print(f"\nStatistiques de {self.__nom} (n°{self.__numero}, {self.__position}):")
        print(f"Buts: {self.__buts}")
        print(f"Passes décisives: {self.__passes}")
        print(f"Cartons jaunes: {self.__cartons_jaunes}")
        print(f"Cartons rouges: {self.__cartons_rouges}")

class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"\nStatistiques de l'équipe de {self.__nom}:")
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, action):
        if joueur in self.__joueurs:
            if action == "but":
                joueur.marquerUnBut()
            elif action == "passe":
                joueur.effectuerUnePasseDecisive()
            elif action == "jaune":
                joueur.recevoirUnCartonJaune()
            elif action == "rouge":
                joueur.recevoirUnCartonRouge()

# Tests
# Équipe de France
zidane = Joueur("Zidane", 10, "Milieu")
thuram = Joueur("Thuram", 4, "Défenseur")
petit = Joueur("Petit", 7, "Milieu")  # Remplace Barthez par Petit

france = Equipe("France")
france.ajouterJoueur(zidane)
france.ajouterJoueur(thuram)
france.ajouterJoueur(petit)

# Équipe du Brésil
ronaldo = Joueur("Ronaldo", 9, "Attaquant")
roberto_carlos = Joueur("Roberto Carlos", 3, "Défenseur")
cafu = Joueur("Cafu", 2, "Défenseur")

bresil = Equipe("Brésil")
bresil.ajouterJoueur(ronaldo)
bresil.ajouterJoueur(roberto_carlos)
bresil.ajouterJoueur(cafu)

print("État initial:")
france.afficherStatistiquesJoueurs()
bresil.afficherStatistiquesJoueurs()

# Simulation d'un match France vs Brésil
print("\nDéroulement du match:")
france.mettreAJourStatistiquesJoueur(thuram, "jaune")  # Tacle un peu dur
bresil.mettreAJourStatistiquesJoueur(roberto_carlos, "passe")  # Centre pour Ronaldo
bresil.mettreAJourStatistiquesJoueur(ronaldo, "but")   # But sur le centre

france.mettreAJourStatistiquesJoueur(zidane, "passe")  # Passe décisive
france.mettreAJourStatistiquesJoueur(thuram, "but")    # But sur la passe de Zidane
bresil.mettreAJourStatistiquesJoueur(cafu, "rouge")    # Tacle dangereux
france.mettreAJourStatistiquesJoueur(zidane, "but")    # But en fin de match

print("\nÉtat final:")
france.afficherStatistiquesJoueurs()
bresil.afficherStatistiquesJoueurs()
