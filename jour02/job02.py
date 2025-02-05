# Objectif du job :
# - Créer une classe Livre avec des attributs privés (titre, auteur, nombre_pages)
# - Implémenter des accesseurs et mutateurs pour ces attributs
# - Ajouter une vérification pour nombre_pages (entier positif uniquement)
#
# Solution :
# - Création d'une classe Livre avec titre, auteur et nombre_pages en privé
# - Implémentation des getters et setters pour chaque attribut
# - Ajout d'une vérification dans set_nombre_pages pour valider la valeur

class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

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

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 93)

print(f"Titre : {livre.get_titre()}")
print(f"Auteur : {livre.get_auteur()}")
print(f"Nombre de pages : {livre.get_nombre_pages()}")

livre.set_nombre_pages(-5)  

livre.set_nombre_pages(100)
print(f"\nNouveau nombre de pages : {livre.get_nombre_pages()}")
