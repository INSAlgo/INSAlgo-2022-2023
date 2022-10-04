def flatlandSpaceStations(n, c):
    c.sort()
    maxi=c[0]
    
    for i in range(len(c)-1):
        maxi = max(maxi,int((c[i+1]-c[i])/2))
    maxi = max(maxi,n-1-c[-1])
    return maxi
