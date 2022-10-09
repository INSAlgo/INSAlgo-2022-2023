def powerSum(X, N):
    
    def recurs(X,N,start):
        count = 0 
        for i in range(start,X):
            ans = X-i**N
            if ans == 0:
                count += 1
            if ans> 0 :
                count += recurs(ans,N,i+1)
            if ans<0:
                break   
        return count
    
    return(rec(X,N,1))
