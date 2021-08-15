
def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in money:
        for j in range(n+1):
            if i > j: continue
            dp[j] += dp[j-i]
    return dp[n]
solution(5, [1,2,5])