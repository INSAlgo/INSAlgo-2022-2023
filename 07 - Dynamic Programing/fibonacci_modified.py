def fibonacciModified(t1, t2, n):
    dp = [-1] * n
    dp[0] = t1
    dp[1] = t2
    for i in range(2,n):
        dp[i] = dp[i-2] + dp[i-1]**2
    print(dp)
    return dp[n-1]