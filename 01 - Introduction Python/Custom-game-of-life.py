import sys
import math

#Mise au propre des entrés
h, w, n = [int(i) for i in input().split()]
alive = input().replace('0','.').replace('1','O')
dead = input().replace('0','.').replace('1','O')

#Lecture de la grille de base
grid = []
for i in range(h):
    grid.append(list(input()))

#Fonction qui return le nombre de voisin en vie
def numOfNeighbours(grid, line, col) -> int:
    ans = 0

    for x in range(-1,2):
        if col+x<0 or col+x>=len(grid[0]):
            continue
        else:
            for y in range(-1,2):
                if line+y<0 or line+y>= len(grid) or (x==0 and y==0):
                    continue
                else:
                    if grid[line+y][col+x]=='O':
                        ans+=1
    return ans

#Boucle sur les n tours
for i in range(n):
    new=[]
    for y in range(h):
        new.append([])
        for x in range(w):
            resNei = numOfNeighbours(grid, y, x)
            if grid[y][x]=='O':
                new[y].append(alive[resNei])
            else:
                new[y].append(dead[resNei])
    grid = new
for line in grid:
    print("".join(line))
