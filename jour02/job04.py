# Objectif du job :
# - Créer une classe Student avec des attributs privés (nom, prenom, num_etudiant, credits)
# - Implémenter une méthode add_credits pour ajouter des crédits (si > 0)
# - Créer une méthode privée __student_eval qui évalue le niveau selon les crédits
# - Implémenter une méthode student_info qui affiche les informations
#
# Solution :
# - Création des attributs privés avec credits initialisé à 0
# - Implémentation de la méthode add_credits avec vérification
# - Méthode privée __student_eval pour l'évaluation
# - Méthode student_info pour l'affichage des informations

class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Erreur : le nombre de crédits doit être supérieur à 0")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__num_etudiant}")
        print(f"Niveau = {self.__level}")

john = Student("John", "Doe", 145)

john.add_credits(10)
john.add_credits(10)
john.add_credits(10)

print(f"Le nombre de credits de John Doe est de {john._Student__credits} points")

# Ajout de crédits supplémentaires pour atteindre le niveau "Bien" (≥ 70 crédits)
john.add_credits(40) 

john.student_info()
