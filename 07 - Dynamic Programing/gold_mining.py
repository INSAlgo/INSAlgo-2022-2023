class Solution:
    def localGold(self, M, n, m, i, j, dp):
        if i < 0 or i == n or j == m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            r = self.localGold(M, n, m, i, j+1, dp)
            ru = self.localGold(M, n, m, i-1, j+1, dp)
            rd = self.localGold(M, n, m, i+1, j+1, dp)
            dp[i][j] = M[i][j] + max(r, ru, rd)
            return dp[i][j]
            
    def maxGold(self, n, m, M):
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        sortie = 0
        for i in range(n):
            sortie = max(sortie, self.localGold(M, n, m, i, 0, dp))
        return sortie
