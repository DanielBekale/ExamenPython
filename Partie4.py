import random
#1)

#fonction saisie

def saisie():
    t = []
    while True:
        nom = input("Nom de la personne (ou 'q' pour quitter) : ")
        if nom == 'q':
            break
        t.append({'nom': nom})
    return t
#2)

#fonction calculAnnee

def calculAnnee(t):
    for personne in t:
        annee_min = int(input("Période - Année minimale : "))
        annee_max = int(input("Période - Année maximale : "))
        personne['annee'] = random.randint(annee_min, annee_max)

#3)

#fonction calculTemps
def calculTemps(t):
    for personne in t:
        annee_depart = personne['annee']
        annee_restante = 2017 - annee_depart

        if annee_restante < 0:
            annee_restante += 10

        temps = abs(annee_restante) * 10
        personne['temps'] = temps

# Fonctions et Procédures
personnes = saisie()
calculAnnee(personnes)
calculTemps(personnes)

# Affichage 
for personne in personnes:
    print("Nom:", personne['nom'])
    print("Année:", personne['annee'])
    print("Temps:", personne['temps'])
    print()


#4) Prendriez vous ce risque?
