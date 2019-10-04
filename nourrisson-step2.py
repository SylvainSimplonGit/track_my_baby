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

config_boys = {
    'weights' : [ ['05', 'poids-age-garcon-0-60.csv', 8],     ['25', 'poids-age-garcon-0-60.csv', 11],     ['50', 'poids-age-garcon-0-60.csv', 12],     ['75', 'poids-age-garcon-0-60.csv', 13],     ['95', 'poids-age-garcon-0-60.csv', 16]     ],
    'heights' : [ ['05', 'taille-age-garcon-0-60.csv', 9],    ['25', 'taille-age-garcon-0-60.csv', 12],    ['50', 'taille-age-garcon-0-60.csv', 13],    ['75', 'taille-age-garcon-0-60.csv', 14],    ['95', 'taille-age-garcon-0-60.csv', 17]    ],
    'skulls' :  [ ['05', 'perim-cra-age-garcon-0-60.csv', 9], ['25', 'perim-cra-age-garcon-0-60.csv', 12], ['50', 'perim-cra-age-garcon-0-60.csv', 13], ['75', 'perim-cra-age-garcon-0-60.csv', 14], ['95', 'perim-cra-age-garcon-0-60.csv', 17] ]
}

config_girls = {
    'weights' : [ ['05', 'poids-age-fille-0-60.csv', 8],      ['25', 'poids-age-fille-0-60.csv', 11],      ['50', 'poids-age-fille-0-60.csv', 12],      ['75', 'poids-age-fille-0-60.csv', 13],      ['95', 'poids-age-fille-0-60.csv', 16]      ],
    'heights' : [ ['05', 'taille-age-fille-0-60.csv', 9],     ['25', 'taille-age-fille-0-60.csv', 12],     ['50', 'taille-age-fille-0-60.csv', 13],     ['75', 'taille-age-fille-0-60.csv', 14],     ['95', 'taille-age-fille-0-60.csv', 17]     ],
    'skulls' :  [ ['05', 'perim-cra-age-fille-0-60.csv', 9],  ['25', 'perim-cra-age-fille-0-60.csv', 12],  ['50', 'perim-cra-age-fille-0-60.csv', 13],  ['75', 'perim-cra-age-fille-0-60.csv', 14],  ['95', 'perim-cra-age-fille-0-60.csv', 17]  ]
}

data_dict = { 'weights':{}, 'heights':{}, 'skulls':{} }

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

    csv_file = open('constantes-nourrissons/' + csv_file_path, "r")
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
        print(f"Sortie sur erreur !")
    finally:
        csv_file.close()

# Demande à l'utilisateur d'entrer le genre
genre = entrer_genre()

# Définition des variables en fonction du genre
if genre == 'g':
    for key, value in config_boys.items():
        for datas in value:
            data_dict[key][datas[0]] = mise_en_liste_constantes(datas[1], datas[2])
else:
    for key, value in config_girls.items():
        for datas in value:
            data_dict[key][datas[0]] = mise_en_liste_constantes(datas[1], datas[2])

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

# Fonction de créationn d'un graphique
def creer_graphique(emplacement, type, place_legend, donnees, marker_type, marker_color, label_x, label_y, liste_axe_y):
    global ages_donnees

    plt.subplot(1, 3, emplacement)

    line1, line2, line3, line4, line5 = plt.plot(
        ages, data_dict[type]['05'], '#448abd',
        ages, data_dict[type]['25'], '#f29739', 
        ages, data_dict[type]['50'], '#59a94a',
        ages, data_dict[type]['75'], '#cf4b3e',
        ages, data_dict[type]['95'], '#9f82c4'
        )

    plt.legend([line1, line2, line3, line4, line5], ['5%', '25%', '50%', '75%', '95%'], loc = place_legend)

    plt.scatter(ages_donnees, donnees, marker = marker_type, color = marker_color)

    plt.ylabel(label_y)
    plt.xlabel(label_x)

    axes = plt.gca()
    axes.xaxis.set_ticks(range(0,len(ages),10))
    axes.yaxis.set_ticks(liste_axe_y)
    axes.xaxis.grid(True, color = '#bdbdbd')
    axes.yaxis.grid(True, color = '#bdbdbd')

# Définition du sous graphique 1
creer_graphique(1, 'weights', 'upper left', weights_donnees, 'o', 'black', "Age en mois", "Poids en kg", [2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5])

# Définition du sous graphique 2
creer_graphique(2, 'heights', 'upper left', heights_donnees, 'o', 'black', "Age en mois", "Taille en cm", range(50, 120, 10))

# Définition du sous graphique 3
creer_graphique(3, 'skulls', 'lower right', skulls_donnees, 'o', 'black', "Age en mois", "Périmètre cranien en cm", range(35, 55, 5))

# Affichage des graphiques
plt.show()