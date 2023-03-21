
def getValues(node):
    if not node:
        return []
    values=[node.data]
    return values+getValues(node.right)+getValues(node.left)

def search(root,value):
    currentNode=root
    while currentNode.data!=value:
        if value>currentNode.data:
            currentNode=currentNode.right
        else:
            currentNode=currentNode.left
        if not currentNode:
            return False
    else:
        return True

def check_binary_search_tree_(root):
    values = getValues(root)
    if len(set(values))!=len(values):
        return False
    for value in values:
        if not search(root,value):
            return False
    else:
        return True
