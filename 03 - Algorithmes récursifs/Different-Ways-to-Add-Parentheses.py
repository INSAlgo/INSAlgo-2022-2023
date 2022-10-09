class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int] :
        n = len(expression)
        if n == 0:
            return []
        elif expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(n):
            if not expression[i].isdigit():
                op = expression[i]
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if op=="+":
                            res.append(l+r)
                        elif op =="-":
                            res.append(l-r)
                        else:
                            res.append(l*r)
        return res  
            
        