class Solution:
    def func(self, n, r, dp):
        if dp[n][r] != -1:
            return dp[n][r]
        if r > n:
            dp[n][r] = 0
            return 0
        if r==0 or r==n:
            dp[n][r] = 1
            return 1
        dp[n][r] = self.func(n-1, r-1, dp) + self.func(n-1, r, dp)
        return dp[n][r]
    
    def nCr(self, n, r):
        dp = [[-1 for _ in range(r+1)] for _ in range(n+1)]
        return self.func(n, r, dp)%(10**9 + 7)