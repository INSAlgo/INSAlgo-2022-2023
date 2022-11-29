
m = int(input())
n = int(input())

Map = [input() for _ in range(m)]

dp = [[ 0 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if Map[i][j] == '0':
            if j > 0:
                dp[i][j] += dp[i][j-1]
            if i > 0:
                dp[i][j] += dp[i-1][j]

print(dp[m-1][n-1])