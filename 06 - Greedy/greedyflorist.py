# strategy : get the most expensive flowers when the multiplier is low and the cheapest when the multiplier is high
def getMinimumCost(k, c):
    c.sort()
    cout=0
    b=k
    multi=1
    for i in range(len(c)-1,-1,-1):
        cout=cout+c[i]*multi
        b=b-1
        if b==0:
            b=k
            multi=multi+1
    return cout
