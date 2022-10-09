class Solution:
     def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
                return False
            
        def isPowOfTwo(num):
            if num%2 != 0:
                if num == 1:
                    return True
                else:
                    return False
            else:
                return(isPowOfTwo(num/2))
        
        return isPowOfTwo(n)
