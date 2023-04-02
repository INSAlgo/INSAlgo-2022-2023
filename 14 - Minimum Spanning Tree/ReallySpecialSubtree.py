""" !!!!!! """
#Besoin d'utiliser la classe UnionFind de Louis Sugy (for mor information -> README.md)

def kruskals(g_nodes, g_from, g_to, g_weight):
    edgeListe = []
    for i in range(len(g_from)):
        edgeListe.append((g_weight[i],g_weight[i]+g_from[i]+g_to[i],(g_from[i],g_to[i])))
    edgeListe.sort(reverse=True)
    
    sets = UnionFind(range(1,g_nodes+1))
    rep=0
    while edgeListe:
        currentEdge = edgeListe.pop()
        if not sets.is_same_set(currentEdge[2][0],currentEdge[2][1]):
            sets.union(currentEdge[2][0],currentEdge[2][1])
            rep+=currentEdge[0]
        
    return rep
    
