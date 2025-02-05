# Objectif du job :
# - Reprendre la classe Livre du job précédent
# - Ajouter un attribut privé disponible initialisé à True
# - Créer une méthode verification() qui retourne la disponibilité
# - Créer des méthodes emprunter() et rendre() pour gérer le prêt
#
# Solution :
# - Ajout de l'attribut disponible initialisé à True
# - Implémentation de la méthode verification()
# - Implémentation des méthodes emprunter() et rendre()

class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
    
    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
    
    def set_nombre_pages(self, nouveau_nombre_pages):
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès")
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès")
        else:
            print("Le livre n'a pas été emprunté")


livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 93)

print("État initial :", "disponible" if livre.verification() else "indisponible")
livre.emprunter()
print("Après emprunt :", "disponible" if livre.verification() else "indisponible")
livre.rendre()
print("Après rendu :", "disponible" if livre.verification() else "indisponible")
