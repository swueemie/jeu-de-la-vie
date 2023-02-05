import os
from random import randint
from time import sleep

""" 
Comment fonctionne le jeu :
Etape 1 : Une grille pleine d'espaces vides sera crée
Etape 2 :init_grille sera alors appelé et avec un pourcentage de 33% définira la valeur "O" sur certains des espaces de la grille
Etape 3 : Chaque seconde le reactualise_grille est appelé et le jeu démarre
Etape 4 : Chaque cellule vérifiera ses propres voisins et, en suivant les règles du jeu, décidera si elle doit mourir, vivre ou naître
Etape 5 : Les nouveaux statuts (vivant ou mort) des cellules seront ajoutés aux tableaux qui à la fin seront mis à jour dans la grille
 """

lignes = range(10) #définir les tailles 
colonnes = range(10) 
grille = [[' ' for x in colonnes] for y in lignes] #initialiser la grille avec des espaces vides

""" 
Fonction qui imprime toutes les valeurs des cellules (de la matrice)
 """
def print_grille():
    for x in lignes:
        for y in colonnes:
            print_cellule(grille[x][y])#matrice
        print()

""" 
Fonction qui crée la disposition du tableau
 """
def print_cellule(cellule):
    print ('[' + cellule + ']',end='') 


""" 
Définit une cellule sur "O" (vivante) avec une probabilité de 33 %
Lorsque cette fonction est appelée, si testchaine est passé en conséquence, cela prédéfinira la grille avec des valeurs à tester

 """
def init_grille(testchaine = ''):
    if(testchaine == 'blinker'): #exemple de motifs qu on peut tester avec "init_grille('blinker')" a la fin
        grille[3][2] = 'O'
        grille[3][3] = 'O'
        grille[3][4] = 'O'
    if(testchaine == 'glider'):
        grille[2][1] = 'O'
        grille[3][2] = 'O'
        grille[3][3] = 'O'
        grille[2][3] = 'O'
        grille[1][3] = 'O'
    
    if(testchaine == ''):
        for x in lignes:
            for y in colonnes:
                rand = randint(0,10)#Nb aleatoire pour que la cellule a 33% de chance de naitre
                if rand <3:
                    grille[x][y] = 'O'

""" 
Cette fonction gère la mise à jour de la génération
Pour que toutes les cellules soient mises à jour correctement, le changement de leurs statut (vivant ou mort) se fait à la fin
et donc on utilise 2 tableaux, un pour mettre à jour le "vivant" et un pour mettre à jour le "mort"
 """
def reactualise_grille():
    seraVivant = []#variable pour enregistrer l indice des cellules vivantes/mortes 
    seraMort = []#pour qu elles deviennent vivantes ou mortes durant la prochaine generation
    for x in lignes: # boucle qui vérifie toute la grille
            for y in colonnes:
                voisins_vivants_liste = get_voisins_vivants_liste(x, y) #Nb de cellules vivantes autour de celle selectionnee
                cellule_presente = grille[x][y]

                if cellule_presente == 'O' and (voisins_vivants_liste < 2 or voisins_vivants_liste > 3): #valeur de cellule dans la boucle
                    seraMort.append([x,y])
                else:
                    if voisins_vivants_liste == 2:
                        seraVivant.append([x,y])
    
    for x in seraVivant:
        grille[x[0]][x[1]] = 'O'

    for x in seraMort:
        grille[x[0]][x[1]] = ' '

    
""" 
Cette fonction renvoie le nombre de toutes les cellules vivantes voisines dans une gamme de 8 en prenant comme paramètre la cellule de depart
Ex : 
[ ][ ][O]
[ ][O][ ]
[ ][ ][O]

La cellule au milieu a 2 voisins vivants 
 """           
def get_voisins_vivants_liste(verifier_ligne, verifier_colonne): #verifier_ligne and verifier_colonne sont les indices de la cellule à vérifier
        obtenir_min= -1 #ces valeurs sont nécessaires pour vérifier les 8 voisins autour
        obtenir_max = 2
        voisin_vivant_liste= -1 # cette valeur commence à -1 car la boucle se comptera elle meme comme un voisin
        for x in range(obtenir_min,obtenir_max):
            for y in range(obtenir_min,obtenir_max):
                voisin_ligne = verifier_ligne + x #pour verifier le prochain voisin
                voisin_colonne = verifier_colonne + y
                
                """ 
               si la cellule verifiée ne dépasse pas la longueur de la grille et qu'elle est vivante
                alors voisin_vivant_liste se mettera a jour
                 """
                if voisin_ligne < len(lignes) - 1 and voisin_colonne < len(colonnes) - 1:
                    if grille[voisin_ligne][voisin_colonne] == 'O':
                        voisin_vivant_liste+= 1
            
        return voisin_vivant_liste



init_grille() #sans motifs, cest aleatoire
while True:
    os.system('cls')
    print_grille()
    reactualise_grille()
    print('Pour arreter le programme : CTRL + C')
    sleep(1)