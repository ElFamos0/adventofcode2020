'''
Les # sont des arbres et les . sont des endroits sans arbres le même pattern se repète vers la droite un nombre incalculable de fois.
On fait une diagonale du type 3 vers la droite et 1 vers le bas mais petit problème sur l'exemple ça pue la merde ! 
'''
with open("inputs/adoc03.txt") as file:
    grid = [line[0:-1] for line in file] #ok donc [0,-1] ça sert bien à enlever le dernier terme on va du premier à l'avant dernier en gros mais du coup ça veut dire que \n compte comme un unique caractère interressant a savoir

def check(right,bottom):
    x,y = 0,0
    count = 0
    while not y>= len(grid)-1: #tant que le petit curseur n'est pas en bas de la map 
        x += right #on ajoute les déplacements
        y += bottom
        if x >= width: # si x dépasse la longueur de la grille on le fait retourner au début en mode full bg
            x -= width
        if grid[y][x]=="#": #si on rencontre un bel arbre 
            count+=1 #on le compte 
    return count 

width = len(grid[0])#on prend comme base de longueur la première ligne puisque que toutes les autres font la même taille. 

print(check(3,1)*check(1,1)*check(5,1)*check(7,1)*check(1,2))
