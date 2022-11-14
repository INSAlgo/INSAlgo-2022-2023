#Here the strategy is to determine the minimal cost at the end of the course
# and to determine step by step the minimal cost before each building. 
def chiefHopper(arr):
    enNecc=[0]
    for lastelem in arr[::-1]:
        enNecc.append(math.ceil((lastelem+enNecc[-1])/2))
    print(enNecc)
    return(enNecc[-1])
