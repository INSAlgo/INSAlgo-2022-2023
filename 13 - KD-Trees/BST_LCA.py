def lca(root, v1, v2):
    currentNode = root
    ma,mi=max(v1,v2),min(v1,v2)
    
    while not(ma>=currentNode.info and mi<=currentNode.info):
        if ma>currentNode.info:
            currentNode=currentNode.right
        else:
            currentNode=currentNode.left
    else:
        return currentNode
