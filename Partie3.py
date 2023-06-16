# 3.1)

# Fonction nbMotsAvecVoyelle qui renvoie le nombre de mot commencant par une voyelle
def nbMotsAvecVoyelle(nomf):
    voyelles = ['a', 'e', 'i', 'o', 'u']
    count = 0

    with open(nomf, 'r') as fichier:
        for mot in fichier:
            mot = mot.strip().lower()  # Suppression et conversion en minuscules
            if mot[0] in voyelles:
                count += 1

    return count


# 3.2)

# Procedure compterChaqueMot qui ecrit tous les mots du fichier1 dans le fichier2
def compterChaqueMot(nomf1, nomf2):
    with open(nomf1, 'r') as fichier1, open(nomf2, 'w') as fichier2:
        mot_precedent = None
        compteur = 0

        for mot in fichier1:
            mot = mot.strip().lower()  # Suppression et conversion en minuscules

            if mot == mot_precedent:
                compteur += 1
            else:
                if mot_precedent is not None:
                    fichier2.write(f"{mot_precedent} {compteur}\n")
                mot_precedent = mot
                compteur = 1

        if mot_precedent is not None:
            fichier2.write(f"{mot_precedent} {compteur}\n")

# Procedure et Procédures
nom_fichier1 = 'fichier1.txt'
nom_fichier2 = 'fichier2.txt'

# Appellons la fonction nbMotsAvecVoyelle
nb_mots_avec_voyelle = nbMotsAvecVoyelle(nom_fichier1)
print("Nombre de mots commençant par une voyelle :", nb_mots_avec_voyelle)

# Appelons la fonction compterChaqueMot
compterChaqueMot(nom_fichier1, nom_fichier2)

# Affichons tous ce qui se trouve dans le fichier2
with open(nom_fichier2, 'r') as fichier2:
    contenu_fichier2 = fichier2.read()
    print("Contenu du fichier2 :\n", contenu_fichier2)
