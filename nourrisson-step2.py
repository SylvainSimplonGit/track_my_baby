#!C:\Python3\python.exe

####################################################################################
#                     Récupération des données CSV
####################################################################################
# csv pour lire les fichiers de données
import csv

# Déclaration des variables
ages = range(61)

ages_donnees = []
weights_donnees = []
heights_donnees = []
skulls_donnees = []

col_weights_05 = 8
col_weights_25 = 11
col_weights_50 = 12
col_weights_75 = 13
col_weights_95 = 16

col_heights_05 = 9
col_heights_25 = 12
col_heights_50 = 13
col_heights_75 = 14
col_heights_95 = 17

col_skulls_05 = 9
col_skulls_25 = 12
col_skulls_50 = 13
col_skulls_75 = 14
col_skulls_95 = 17

# IHM pour connaitre le genre à afficher
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

# Récupération des mesures dans les fichiers à faire
def mise_en_liste_constantes(csv_file_path, col):
    index = 0
    temp_liste = []

    csv_file = open(csv_file_path, "r")
    try:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            if index > 0:
                temp_liste.append(float(row[col-1]))
            index += 1
    except:
        print(f"Sortie sur erreur !")
    finally:
        csv_file.close()
        return temp_liste

def mise_en_liste_donnees(csv_file_path):
    index_csv = 0
    
    global ages_donnees, weights_donnees, heights_donnees, skulls_donnees

    csv_file = open(csv_file_path, "r")
    try:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            if index_csv > 0:
                # Prendre la première colonne pour connaitre le mois
                ages_donnees.append(int(row[0]))
                weights_donnees.append(float(row[1]))
                heights_donnees.append(float(row[2]))
                skulls_donnees.append(float(row[3]))
            index_csv += 1
    except:
        print(f"Sortie sur : {ValueError} !")
    finally:
        csv_file.close()

# Demande à l'utilisateur d'entrer le genre
genre = entrer_genre()

# Définition des variables en fonction du genre
if genre == 'g':
    weights_05 = mise_en_liste_constantes('constantes-nourrissons\poids-age-garcon-0-60.csv', col_weights_05)
    weights_25 = mise_en_liste_constantes('constantes-nourrissons\poids-age-garcon-0-60.csv', col_weights_25)
    weights_50 = mise_en_liste_constantes('constantes-nourrissons\poids-age-garcon-0-60.csv', col_weights_50)
    weights_75 = mise_en_liste_constantes('constantes-nourrissons\poids-age-garcon-0-60.csv', col_weights_75)
    weights_95 = mise_en_liste_constantes('constantes-nourrissons\poids-age-garcon-0-60.csv', col_weights_95)

    heights_05 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-garcon-0-60.csv', col_heights_05)
    heights_25 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-garcon-0-60.csv', col_heights_25)
    heights_50 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-garcon-0-60.csv', col_heights_50)
    heights_75 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-garcon-0-60.csv', col_heights_75)
    heights_95 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-garcon-0-60.csv', col_heights_95)

    skulls_05 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-garcon-0-60.csv', col_skulls_05)
    skulls_25 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-garcon-0-60.csv', col_skulls_25)
    skulls_50 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-garcon-0-60.csv', col_skulls_50)
    skulls_75 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-garcon-0-60.csv', col_skulls_75)
    skulls_95 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-garcon-0-60.csv', col_skulls_95)
else:
    weights_05 = mise_en_liste_constantes('constantes-nourrissons\poids-age-fille-0-60.csv', col_weights_05)
    weights_25 = mise_en_liste_constantes('constantes-nourrissons\poids-age-fille-0-60.csv', col_weights_25)
    weights_50 = mise_en_liste_constantes('constantes-nourrissons\poids-age-fille-0-60.csv', col_weights_50)
    weights_75 = mise_en_liste_constantes('constantes-nourrissons\poids-age-fille-0-60.csv', col_weights_75)
    weights_95 = mise_en_liste_constantes('constantes-nourrissons\poids-age-fille-0-60.csv', col_weights_95)

    heights_05 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-fille-0-60.csv', col_heights_05)
    heights_25 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-fille-0-60.csv', col_heights_25)
    heights_50 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-fille-0-60.csv', col_heights_50)
    heights_75 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-fille-0-60.csv', col_heights_75)
    heights_95 = mise_en_liste_constantes('constantes-nourrissons\\taille-age-fille-0-60.csv', col_heights_95)

    skulls_05 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-fille-0-60.csv', col_skulls_05)
    skulls_25 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-fille-0-60.csv', col_skulls_25)
    skulls_50 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-fille-0-60.csv', col_skulls_50)
    skulls_75 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-fille-0-60.csv', col_skulls_75)
    skulls_95 = mise_en_liste_constantes('constantes-nourrissons\perim-cra-age-fille-0-60.csv', col_skulls_95)

mise_en_liste_donnees('mesures.csv')

####################################################################################
#                     Affichage du graphique
####################################################################################
# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt

# Couleurs
# 5%    #448abd
# 25%   #f29739
# 50%   #59a94a
# 75%   #cf4b3e
# 95%   #9f82c4
# Couleur de quadrillage    #bdbdbd

# Définition de la Figure
plt.figure(1)

# Définition du sous graphique 1
plt.subplot(1,3,1)

line1, line2, line3, line4, line5 = plt.plot(ages, weights_05, '#448abd',
    ages, weights_25, '#f29739', 
    ages, weights_50, '#59a94a',
    ages, weights_75, '#cf4b3e',
    ages, weights_95, '#9f82c4'
    )
plt.legend([line1, line2, line3, line4, line5], ['5%', '25%', '50%', '75%', '95%'], loc = 'upper left')

plt.scatter(ages_donnees, weights_donnees, marker = 'o', color = 'black')

plt.ylabel("Poids en kg")
plt.xlabel("Age en mois")

axes = plt.gca()
axes.xaxis.set_ticks(range(0,len(ages),10))
axes.yaxis.set_ticks([2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5])
axes.xaxis.grid(True, color = '#bdbdbd')
axes.yaxis.grid(True, color = '#bdbdbd')

# Définition du sous graphique 2
plt.subplot(1,3,2)

line1, line2, line3, line4, line5 = plt.plot(ages, heights_05, '#448abd',
    ages, heights_25, '#f29739', 
    ages, heights_50, '#59a94a',
    ages, heights_75, '#cf4b3e',
    ages, heights_95, '#9f82c4'
    )
plt.legend([line1, line2, line3, line4, line5], ['5%', '25%', '50%', '75%', '95%'], loc = 'upper left')

plt.scatter(ages_donnees, heights_donnees, marker = 'o', color = 'black')

plt.ylabel("Taille en cm")
plt.xlabel("Age en mois")

axes = plt.gca()
axes.xaxis.set_ticks(range(0,len(ages),10))
axes.yaxis.set_ticks(range(50, 120, 10))
axes.xaxis.grid(True, color = '#bdbdbd')
axes.yaxis.grid(True, color = '#bdbdbd')

# Définition du sous graphique 3
plt.subplot(1,3,3)

line1, line2, line3, line4, line5 = plt.plot(ages, skulls_05, '#448abd',
    ages, skulls_25, '#f29739', 
    ages, skulls_50, '#59a94a',
    ages, skulls_75, '#cf4b3e',
    ages, skulls_95, '#9f82c4'
    )
plt.legend([line1, line2, line3, line4, line5], ['5%', '25%', '50%', '75%', '95%'], loc = 'lower right')

plt.scatter(ages_donnees, skulls_donnees, marker = 'o', color = 'black')

plt.ylabel("Périmètre cranien en cm")
plt.xlabel("Age en mois")

axes = plt.gca()
axes.xaxis.set_ticks(range(0,len(ages),10))
axes.yaxis.set_ticks(range(35, 55, 5))
axes.xaxis.grid(True, color = '#bdbdbd')
axes.yaxis.grid(True, color = '#bdbdbd')

# Affichage des graphiques
plt.show()