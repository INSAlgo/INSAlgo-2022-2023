#Lecture des inputs et debut des boucles
for i in range(int(input())):
    n = int(input())
    
    #Edge case 1: n=1 donc non premier
    if(n==1):
        print("Not prime")
    #Edge case 2: n=2 donc premier
    if(n==2):
        print("Prime")
    #Autres cas : on verifie tous les diviseurs entre 2 et sqrt(n)
    #Pas besoin de verifier plus car si n=a*b et que a > sqrt(n) alors focement b < sqrt(n) et donc à deja été vu
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                print("Not prime")
                break
        else:
            print("Prime")
