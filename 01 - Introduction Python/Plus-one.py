class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #i = -1 Pour partir de la fin 
        i = -1
        
        #On verifie si avec l'addition, on passe à 10 (besoin de reporté le reste)
        while digits[i]+1== 10:
            #On met le digit en question a 0, et on passe qu digit suivant (decrementation du i)
            digits[i]=0
            i-=1
            
            #Si on arrive à la fin du tableau, on break la boucle
            if i<-len(digits):
                break
                
        #Dans un boucle, le else s'execute a la fin si l'on est pas sorti avec un break (~if not break then)
        else:
            #Si l'on pass ici, c'est qu'un digit+1 ne fesait pas 10, on l'incremente donc et on return la solution
            digits[i]+=1
            return digits
        
        #Si l'on atteint ici, c'est qu'on à atteint la fin du tableau sans pouvoir incrementer un digit
        #On rajoute un 1 devant le tableau qui normalement ne contient plus que des 0
        digits=[1]+digits
        return digits
