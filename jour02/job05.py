# Objectif du job :
# - Créer une classe Voiture avec des attributs privés (marque, modele, annee, kilometrage)
# - Implémenter des méthodes demarrer() et arreter() qui modifient en_marche
# - Créer une méthode privée verifier_plein() qui vérifie le reservoir
#
# Solution :
# - Création des attributs avec en_marche initialisé à False
# - Implémentation des getters et setters pour chaque attribut
# - Méthode demarrer() qui vérifie le niveau du reservoir
# - Méthode arreter() qui met en_marche à False

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Getters
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    # Setters
    def set_marque(self, marque):
        self.__marque = marque
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Méthode privée
    def __verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture demarre")
        else:
            print("Niveau de carburant insuffisant pour demarrer")

    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrete")


ma_voiture = Voiture("Peugeot", "208", 2020, 50000)

print(f"Etat initial : {'en marche' if ma_voiture.get_en_marche() else 'arretee'}")
ma_voiture.demarrer()
print(f"Apres demarrage : {'en marche' if ma_voiture.get_en_marche() else 'arretee'}")
ma_voiture.arreter()
print(f"Apres arret : {'en marche' if ma_voiture.get_en_marche() else 'arretee'}")
