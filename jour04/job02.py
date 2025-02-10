# Objectif du job :
# - Réutiliser les classes du job01
# - Créer un élève qui dit bonjour et va en cours
# - Modifier son âge à 15 ans
# - Créer un professeur de 40 ans qui commence son cours
#
# Solution :
# - Import des classes du job01
# - Création d'un élève avec les actions demandées
# - Création d'un professeur avec les actions demandées
# - Affichage clair des âges et actions

from job01 import Personne, Eleve, Professeur

print("=== Scénario avec l'élève ===")
eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
print("L'élève a maintenant:", end=" ")
eleve.afficherAge()

print("\n=== Scénario avec le professeur ===")
professeur = Professeur("Mathématiques")
professeur.modifierAge(40)
print("Le professeur a:", end=" ")
professeur.afficherAge()
professeur.bonjour()
professeur.enseigner()
