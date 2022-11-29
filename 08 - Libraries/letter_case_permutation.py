import itertools

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        l=set()
        
        for i in itertools.product('01',repeat=len(S)):
            S2=""
            
            for j in range(len(i)):
                S2+= S[j].upper()  if i[j]=='1' else S[j].lower()
            
            l.add(S2)
        
        return(list(l))
