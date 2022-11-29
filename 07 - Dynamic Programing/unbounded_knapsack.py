def unboundedKnapsack(k, arr, n):
    dp = [[0 for i in range(k+1)] for j in range(n+1)]
    arr = [0] + arr
    for i in range(1,n+1):
        for j in range(1, k+1):
            if j >= arr[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-arr[i]] + arr[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][k]