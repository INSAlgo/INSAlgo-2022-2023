class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        def kp(W, wt, val, n):
            KP = [[0 for i in range(W+1)] for j in range(n+1)]
            for i in range(n+1):
                for w in range(W+1):
                    if i == 0 or w == 0:
                        KP[i][w] = 0
                    elif wt[i-1] <= w:
                        KP[i][w] = max(KP[i-1][w], val[i-1] + KP[i-1][w-wt[i-1]])
                    else:
                        KP[i][w] = KP[i-1][w]
            return KP[n][W]
        return kp(W, wt, val, n)  