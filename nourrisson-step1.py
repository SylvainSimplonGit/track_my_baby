#!C:\Python3\python.exe
import nourrisson_normes

# Fonction pour valider que la valeur val est un entier
def isInteger(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# Fonction pour valider que la valeur val est un décimal
def isFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

# Fonction pour valider le genre entré
def entrer_genre():
    # Demande le genre à l'utilisateur une 1ère fois
    genre = input("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille) : ")
    # Tant que l'entrée n'est pas 'g' ou 'f' on redemande une nouvelle entrée
    while genre != 'g' and genre != 'f':
        # Affichage du message d'erreur de saisie en rappeleant l'entrée
        print(f"Erreur de saisie : {genre} ne fait pas partie des choix possibles !")
        genre = input("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille) : ")
    # Renvoi de l'entrée validée
    return genre

# Fonction pour valider l'age entré
def entrer_age():
    # Demande l'age à l'utilisateur une 1ère fois
    age = input("Veuillez entrer l'age de votre nourrisson en mois (entre 0 et 60 mois) : ")
    # Tant que l'entrée n'est pas un entier compris entre 0 et 60 on redemande une nouvelle entrée
    while not isInteger(age) or int(age) < 0 or int(age) > 60:
        # Affichage du message d'erreur de saisie en rappeleant l'entrée
        print(f"Erreur de saisie : {age} ne fait pas partie des choix possibles !")
        age = input("Veuillez entrer l'age de votre nourrisson en mois (entre 0 et 60 mois) : ")
    # Renvoi de l'entrée validée converti en entier
    return int(age)

# Fonction pour valider le poids entré
def entrer_poids():
    # Demande le poids à l'utilisateur une 1ère fois
    poids = input("Veuillez entrer le poids de votre nourrisson en kg : ")
    # Tant que l'entrée n'est pas un float ou un entier et qu'il n'est pas positif on redemande l'entrée
    while not (isFloat(poids) or isInteger(poids)) or float(poids) < 0:
        # Affichage du message d'erreur de saisie en rappeleant l'entrée
        print(f"Erreur de saisie : {poids} ne fait pas partie des choix possibles !")
        poids = input("Veuillez entrer le poids de votre nourrisson en kg : ")
    # Renvoi de l'entrée validée converti en décimal
    return float(poids)
    
# Fonction pour valider la taille entrée
def entrer_taille():
    # Demande la taille à l'utilisateur une 1ère fois
    taille = input("Veuillez entrer la taille de votre nourrisson en cm : ")
    # Tant que l'entrée n'est pas un float ou un entier et qu'il n'est pas positif on redemande l'entrée
    while not (isFloat(taille) or isInteger(taille)) or float(taille) < 0:
        # Affichage du message d'erreur de saisie en rappeleant l'entrée
        print(f"Erreur de saisie : {taille} ne fait pas partie des choix possibles !")
        taille = input("Veuillez entrer la taille de votre nourrisson en cm : ")
    # Renvoi de l'entrée validée converti en décimal
    return float(taille)
    
# Fonction pour valider le tour du crane entré
def entrer_crane():
    # Demande le tour du crane à l'utilisateur une 1ère fois
    crane = input("Veuillez entrer le périmètre cranien de votre nourrisson en cm : ")
    # Tant que l'entrée n'est pas un float ou un entier et qu'il n'est pas positif on redemande l'entrée
    while not (isFloat(crane) or isInteger(crane)) or float(crane) < 0:
        # Affichage du message d'erreur de saisie en rappeleant l'entrée
        print(f"Erreur de saisie : {crane} ne fait pas partie des choix possibles !")
        crane = input("Veuillez entrer le périmètre cranien de votre nourrisson en cm : ")
    # Renvoi de l'entrée validée converti en décimal
    return float(crane)

# Fonction pour afficher la réponse du poids normé
def message_norme_genre(genre):
    # Choix d'une partie variable du message en fonction du genre
    if genre == 'g':
        message_genre = "un garçon de"
    else:
        message_genre = "une fille de"
    # Renvoi du message en clair
    return message_genre

# Fonction pour afficher la réponse normé ou non
def message_norme_ou_pas(valeur, valeur_mini, valeur_maxi):
    # Choix d'une partie variable du message en fonction de son emplacement dans la norme
    if valeur > valeur_mini and valeur < valeur_maxi:
        message_norme = "est dans la norme !"
    else:
        message_norme = "n'est pas dans la norme !"
    # Renvoi du message en clair
    return message_norme

# Fonction pour afficher la réponse du poids normé
def message_norme_poids(genre, age, poids, poids_mini, poids_maxi):
    # Choix d'une partie variable du message en fonction du genre
    message_genre = message_norme_genre(genre)
    # Choix d'une partie variable du message en focntion de son emplacement dans la norme
    message_norme = message_norme_ou_pas(poids, poids_mini, poids_maxi)
    # Définition des lignes complètes des messages
    ligne_1 = f"La norme de poids pour {message_genre} {age} mois est située entre {poids_mini} kg et {poids_maxi} kg"
    ligne_2 = f"Le poids de votre nourrisson ({poids} kg) {message_norme}"
    # Concatenation des 2 lignes
    message = ligne_1 + '\n' + ligne_2
    # Renvoi du message en clair
    return message

# Fonction pour afficher la réponse de la taille normée
def message_norme_taille(genre, age, taille, taille_mini, taille_maxi):
    # Choix d'une partie variable du message en fonction du genre
    message_genre = message_norme_genre(genre)
    # Choix d'une partie variable du message en focntion de son emplacement dans la norme
    message_norme = message_norme_ou_pas(taille, taille_mini, taille_maxi)
    # Définition des lignes complètes des messages
    ligne_1 = f"La norme de taille pour {message_genre} {age} mois est située entre {taille_mini} cm et {taille_maxi} cm"
    ligne_2 = f"Le taille de votre nourrisson ({taille} cm) {message_norme}"
    # Concatenation des 2 lignes
    message = ligne_1 + '\n' + ligne_2
    # Renvoi du message en clair
    return message

# Fonction pour afficher la réponse du tour de crane normé
def message_norme_crane(genre, age, crane, crane_mini, crane_maxi):
    # Choix d'une partie variable du message en fonction du genre
    message_genre = message_norme_genre(genre)
    # Choix d'une partie variable du message en focntion de son emplacement dans la norme
    if poids > poids_mini and poids < poids_maxi:
        message_norme = "est dans la norme !"
    else:
        message_norme = "n'est pas dans la norme !"
    # Définition des lignes complètes des messages
    ligne_1 = f"La norme du périmètre cranien pour {message_genre} {age} mois est située entre {crane_mini} cm et {crane_maxi} cm"
    ligne_2 = f"Le périmètre cranien de votre nourrisson ({crane} cm) {message_norme}"
    # Concatenation des 2 lignes
    message = ligne_1 + '\n' + ligne_2
    # Renvoi du message en clair
    return message

# Affichage du message d'accueil
print("Bienvenue dans ce programme de vérification des constantes de votre nourisson !")

# Définition des différentes variable par l'utilisateur
genre = entrer_genre()
age = entrer_age()
poids = entrer_poids()
taille = entrer_taille()
crane = entrer_crane()

# Récupération des valeurs dans les tableaux de référence à l'index correspond à l'age en mois
if genre == 'g':
    poids_mini = nourrisson_normes.low_weights_boys[age]
    poids_maxi = nourrisson_normes.high_weights_boys[age]
    taille_mini = nourrisson_normes.low_heights_boys[age]
    taille_maxi = nourrisson_normes.high_heights_boys[age]
    crane_mini = nourrisson_normes.low_skulls_boys[age]
    crane_maxi = nourrisson_normes.high_skulls_boys[age]
else:
    poids_mini = nourrisson_normes.low_weights_girls[age]
    poids_maxi = nourrisson_normes.high_weights_girls[age]
    taille_mini = nourrisson_normes.low_heights_girls[age]
    taille_maxi = nourrisson_normes.high_heights_girls[age]
    crane_mini = nourrisson_normes.low_skulls_girls[age]
    crane_maxi = nourrisson_normes.high_skulls_girls[age]

# Affiche une ligne vide
print()
# Affichage des différents messages re réponse
print(message_norme_poids(genre, age, poids, poids_mini, poids_maxi))
print()
print(message_norme_taille(genre, age, taille, taille_mini, taille_maxi))
print()
print(message_norme_crane(genre, age, crane, crane_mini, crane_maxi))