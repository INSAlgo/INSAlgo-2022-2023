def numberOfPaths(self, m, n):
		
    #memoire pour pas recalculer les meme cases
		mem = [[-1 for _ in range(m)]for _ in range(n)]
		
    #fonction recursive
		def nop(m,n):
      #condition de retour
		    if m==1 or n==1:return 1
		    else:
          #memoire
		        if mem[n-1][m-1]==-1:
              #recursion
		            mem[n-1][m-1]=(nop(m-1,n)+nop(m,n-1))%(10**9+7)
                #retour
		        return mem[n-1][m-1]
		    
		return nop(m,n)
