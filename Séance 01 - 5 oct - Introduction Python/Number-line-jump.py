def kangaroo(x1, v1, x2, v2):
    #Principe :
    #On a deux suite: x1+t*v1 et x2+t*v2
    #On cherche a savoir si ces deux suites s'intesecte pour un ENTIER POSITIF
    # x1+t*v1 = x2+t*v2 <=> x1-x2 = t(v2-v1) <=> t = (x1-x2)/(v2-v1)
    
    #On voit que si v1 = v2 on a division par 0 (les deux kangourous se deplaces a la meme vitesse donc pas d'intersection donc NO)
    if  v1 == v2:
        return "NO"
    else:
        #Verification si t est un entier, et si t est positif
        if float(x1-x2)/float(v2-v1)==int((x1-x2)/(v2-v1)) and int((x1-x2)/(v2-v1))>0:
            return "YES"
        else:
            return "NO"
