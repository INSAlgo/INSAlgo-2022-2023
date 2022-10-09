class Solution:
    
    def subOfSubTree(self, root: TreeNode, sommes):
        sommeDroite,sommeGauche=0,0
        if root.right!=None:
          #Recursion sur le sous arbre de droite
            sommeDroite=self.subOfSubTree(root.right,sommes)
        if root.left!=None:
          #Recursion sur le sous arbre de gauche
            sommeGauche=self.subOfSubTree(root.left,sommes)
        
        #Calcul et ajout de la somme du sous arbre
        total=sommeDroite+sommeGauche+root.val
        sommes.append(total)
        return total
    
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sommes=[]
        if root==None:
            return []
        
        self.subOfSubTree(root,sommes)
        
        #Recuperation des sub sum les plus courantes
        counter=Counter(sommes).most_common()
        reponses=[]
        for i in counter:
            if i[1]==counter[0][1]:

                reponses.append(i[0])
            else:
                break
        return reponses
