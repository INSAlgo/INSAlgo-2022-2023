def insert(self, val):
        if not self.root:
            self.root=Node(val)
            return
        currentNode = self.root
        
        while(1):
            if val<currentNode.info:
                if currentNode.left:
                    currentNode=currentNode.left
                else:
                    currentNode.left = Node(val)
                    break
            else:
                if currentNode.right:
                    currentNode=currentNode.right
                else:
                    currentNode.right = Node(val)
                    break
