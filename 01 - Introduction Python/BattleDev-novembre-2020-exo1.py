import sys

N = int(input())
compteur = 0
for i in range(N):
    #On recupere chaque nom
    nom = input()
    
    #On regarde un à un 5 derniers elements
    for j in range(5):
        
        #Si le caractère n'est pas un chiffre, on quitte la boucle (pas suspect)
        if nom[-j-1] not in "0123456789":
            break
    #Si on a pas break la boucle (les 5 caractères sont des chiffres), alors on a trouvé un compte suspect
    else:
        compteur +=1
'''
Solution avancé en utilisant une regex
import re
for i in range(N):
    if re.fullmatch(r"\d+",input()[-5:]):
        compteur+=1
'''
print(compteur)
