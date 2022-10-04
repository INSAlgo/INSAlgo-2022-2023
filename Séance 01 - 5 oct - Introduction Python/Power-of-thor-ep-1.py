import sys
import math

light_x, light_y, initial_tx, initial_ty = input().split()
light_x = int(light_x)
light_y = int(light_y)
initial_tx = int(initial_tx)
initial_ty = int(initial_ty)
#Methode alternative : light_x, light_y, initial_tx, initial_ty = [int(i) ofr i in input().split()]
#Ou light_x, light_y, initial_tx, initial_ty = list(map(int,input().split()))

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    posX=initial_tx
    posY=initial_ty

    #Boucle tant que Thor n'est pas à la bonne position
    while(posX!=light_x or posY!=light_y):
        
        #initialisation de la variable de sortie
        sortie=""

        #Thor doit aller au Nord/Sud ->
        #On rajoute 'N'/'S' à la sortie
        #On met à jours la position y de Thor
        if light_y>posY:
            sortie+="S"
            posY+=1
        elif light_y<posY:
            sortie+="N"
            posY-=1

        #Thor doit aller a l'Est/West ->
        #On rajoute 'E'/'W' à la sortie
        #On met à jours la position x de Thor
        if light_x>posX:
            sortie+="E"
            posX+=1
        elif light_x<posX:
            sortie+="W"
            posX-=1
        
        #On print la réponse pour ce tour là
        print(sortie)

        #Note: Il est aussi possible de faire 8 tests pour chacune des 8 directions (4 diagonales, 4 orthogonales)
