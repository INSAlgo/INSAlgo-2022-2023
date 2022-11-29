from collections import Counter

class Solution:
    
    def subOfSubTree(self, root: TreeNode, sommes):
        sommeDroite,sommeGauche=0,0
        if root.right!=None:
            sommeDroite=self.subOfSubTree(root.right,sommes)
        if root.left!=None:
            sommeGauche=self.subOfSubTree(root.left,sommes)
        
        total=sommeDroite+sommeGauche+root.val
        sommes.append(total)
        return total
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sommes=[]
        if root==None:
            return []
        
        self.subOfSubTree(root,sommes)
        
        counter=Counter(sommes).most_common()
        reponses=[]
        for i in counter:
            if i[1]==counter[0][1]:

                reponses.append(i[0])
            else:
                break
        return reponses
