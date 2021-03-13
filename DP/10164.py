# 이런 문제에 25분? 아깝다 아까워
n, m, k = map(int, input().split())
if k == 0:
    k = n*m
dp = [0]*(n*m+1)
dp[1] = 1
for i in range(1, k):
    if i%m != 0:
        dp[i+1] += dp[i]
    if (i-1)//m < n-1:
        dp[i+m] += dp[i]
a = dp[k]
dp = [0]*(n*m+1)
dp[k] = 1
for i in range(k, n*m+1):
    if i%m != 0:
        dp[i+1] += dp[i]
    if (i-1)//m < n-1:
        dp[i+m] += dp[i]
print(dp[n*m]*a)
