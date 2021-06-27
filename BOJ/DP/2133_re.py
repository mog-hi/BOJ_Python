n = int(input())
if n%2 == 1:
    print(0)
else:
    dp = [0]*(31)
    dp[0] = 1
    dp[2] = 3
    dp[4] = dp[2]*dp[2] + 2
    for i in range(6, n+1):
        dp[i] = dp[i-2]*3
        for j in range(4, i+1, 2):
            dp[i] += dp[i-j]*2
    print(dp[n])
