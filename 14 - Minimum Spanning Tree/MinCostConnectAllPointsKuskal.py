#use the UnionFind class (see README.md for more infos)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        edges=[]
        
        for i in range(n-1):
            for j in range(i+1,n):
                edges.append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i,j))
        edges.sort(reverse=True)
        
        
        uf = UnionFind(range(n))
        rep = 0
        
        while edges:
            currentEdge = edges.pop()
            
            if not uf.is_same_set(currentEdge[2],currentEdge[1]):
                uf.union(currentEdge[2],currentEdge[1])
                rep+=currentEdge[0]
        return(rep)
