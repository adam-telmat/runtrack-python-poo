# Objectif du job :
# - Créer une classe Tache avec titre, description et statut
# - Créer une classe ListeDeTaches pour gérer une liste de tâches
# - Implémenter les méthodes de gestion (ajouter, supprimer, marquer comme finie)
# - Implémenter les méthodes d'affichage et de filtrage
#
# Solution :
# - Création des classes avec attributs privés
# - Implémentation des méthodes de gestion demandées
# - Tests montrant toutes les fonctionnalités

class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "à faire"  

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache):
        self.__taches.append(tache)
        print(f"Tâche '{tache._Tache__titre}' ajoutée")

    def supprimerTache(self, tache):
        if tache in self.__taches:
            self.__taches.remove(tache)
            print(f"Tâche '{tache._Tache__titre}' supprimée")

    def marquerCommeFinie(self, tache):
        if tache in self.__taches:
            tache._Tache__statut = "terminée"
            print(f"Tâche '{tache._Tache__titre}' marquée comme terminée")

    def afficherListe(self):
        print("\nToutes les tâches:")
        for tache in self.__taches:
            print(f"Tâche: {tache._Tache__titre}")
            print(f"Description: {tache._Tache__description}")
            print(f"Statut: {tache._Tache__statut}\n")

    def filterListe(self, statut):
        taches_filtrees = [tache for tache in self.__taches if tache._Tache__statut == statut]
        print(f"\nTâches avec statut '{statut}':")
        for tache in taches_filtrees:
            print(f"- {tache._Tache__titre}")
            print(f"  Description: {tache._Tache__description}")

# Tests
tache1 = Tache("Révision Python", "Faire les exercices du jour 3")
tache2 = Tache("Pause déjeuner", "Manger et se reposer")
tache3 = Tache("Sport", "Séance de 1 heure")

liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

liste.supprimerTache(tache2)  

liste.marquerCommeFinie(tache1) 

liste.afficherListe()

liste.filterListe("à faire")
