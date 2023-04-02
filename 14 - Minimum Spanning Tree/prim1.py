def prims(n, edges, start):
    # Write your code here
    adj=[[] for _ in range(n+1)]
    for edge in edges:
        adj[edge[0]].append((edge[1],edge[2]))
        adj[edge[1]].append((edge[0],edge[2]))
    
    nodesInTree = {start}
    
    availableEdges = []
    for edge in adj[start]:
        heapq.heappush(availableEdges,(edge[1],start,edge[0]))
    rep=0
    while(len(nodesInTree)<n):
        currentEdge=heapq.heappop(availableEdges)
        
        if currentEdge[2] not in nodesInTree:
            nodesInTree.add(currentEdge[2])
            rep+=currentEdge[0]
            for edge in adj[currentEdge[2]]:
                if edge[0] not in nodesInTree:
                    heapq.heappush(availableEdges,(edge[1],currentEdge[2],edge[0]))
    return rep
