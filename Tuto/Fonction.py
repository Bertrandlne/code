# Définition de la fonction salaire_mensuel
def salaire_mensuel(salaire_annuel):
   salaire_mensuel = salaire_annuel / 12
   return salaire_mensuel

# Définition de la fonction salaire_hebdomadaire
def salaire_hebdomadaire(salaire_mensuel):
   salaire_hebdomadaire = salaire_mensuel / 4
   return salaire_hebdomadaire

# Définition de la fonction salaire_horaire
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

# Demande à l'utilisateur de saisir son salaire annuel
salaire_annuel = float(input("Entrez votre salaire annuel : "))
# Demande à l'utilisateur de saisir le nombre d'heures travaillées par semaine
heures_travaillees = float(input("Entrez le nombre d'heures travaillées par semaine : "))

# Calcul du salaire horaire
mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)

# Affichage du résultat
print("Votre salaire horaire est de", horaire, "euros.")
