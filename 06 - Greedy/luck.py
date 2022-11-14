def luckBalance(k, contests):

    luck = 0
    important = []

    for i in range(len(contests)):
        if contests[i][1] == 0: #si pas important 
            luck += contests[i][0] # go perdre direct
        else:
            important.append(contests[i][0]) #si non on garde dans une autre liste 
        
    important = sorted(important, reverse=True) #trier en decroissant
            
    for i in important:
        if k > 0: # go perdre les plus high
            luck += i
            k -= 1
        else: # et gagner les plus low
            luck -= i

    return luck
