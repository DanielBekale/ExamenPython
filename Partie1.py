#1)voici la structure correspondant a la personne a l'aide des informations citees
#précédement

personne = {
    'nom': '',
    'prenom': '',
    'numéro': '',
    'nom_rue': '',
    'numéro_téléphone': '',
    'code_postal': '',
    'ville': ''
}

#2) Le Programme de gestion d'un annuaire

#Fonction saisie_tab
def saisie_tab():
    annuaire = []
    while True:
        personne = {}
        personne['nom'] = input("Nom: ")
        personne['prenom'] = input("Prénom: ")
        personne['numero'] = input("Numéro dans la rue: ")
        personne['nom_rue'] = input("Nom de la rue: ")
        personne['numero_telephone'] = input("Numéro de téléphone: ")
        personne['code_postal'] = input("Code postal: ")
        personne['ville'] = input("Ville: ")
        
        annuaire.append(personne)
        
        continuer = input("Voulez-vous ajouter une autre personne à l'annuaire? (Oui/Non): ")
        if continuer.lower() != "oui":
            break
    
    return annuaire

# Fonction pour remplir les criteres de recherche
def critere_recherche():
    print("Critères de recherche disponibles:")
    print("1. Nom")
    print("2. Prénom")
    print("3. Nom de la rue")
    print("4. Numéro de téléphone")
    print("5. Code postal")
    print("6. Ville")
    
    choix = input("Choisissez le critère de recherche (entre 1-6): ")
    return choix

#Fonction de recherche
def recherche(annuaire, critere):
    valeur_recherche = input("Entrez la valeur de recherche: ")
    resultat = []
    
    for personne in annuaire:
        if personne[critere] == valeur_recherche:
            resultat.append(personne)
    
    return resultat


#ici nous avons la fonction affiche_tab


def affiche_tab(annuaire, resultat_recherche):
    for personne, resultat in zip(annuaire, resultat_recherche):
        if resultat:
            print("Nom:", personne['nom'])
            print("Prénom:", personne['prenom'])
            print("Numéro dans la rue:", personne['numero'])
            print("Nom de la rue:", personne['nom_rue'])
            print("Numéro de téléphone:", personne['numero_telephone'])
            print("Code postal:", personne['code_postal'])
            print("Ville:", personne['ville'])
            print()


#Menu
annuaire = saisie_tab()
critere = critere_recherche()
resultat_recherche = recherche(annuaire, critere)
affiche_tab(annuaire, resultat_recherche)
