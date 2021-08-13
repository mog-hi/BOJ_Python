def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n == 1: return dp[1]
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567