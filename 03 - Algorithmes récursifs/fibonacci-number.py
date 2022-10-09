def fib(self, n: int) -> int:
        
        def F(i):
            
            if i==0:return 0
            if i==1:return 1
            return F(i-1)+F(i-2)
        
        return F(n)
