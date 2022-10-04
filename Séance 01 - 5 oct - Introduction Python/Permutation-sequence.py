from math import factorial, ceil
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numberSet=list(map(str,range(1,n+1)))
        ans=""
        for i in range(n):
            
            ans+=numberSet.pop(ceil(k/factorial(n-i-1))-1)
            
            k=k%factorial(n-i-1)
        return ans
