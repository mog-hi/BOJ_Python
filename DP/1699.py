n = int(input())
dp = [x for x in range(n+1)]
i = 1
for i in range(2, n+1):
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i], dp[i-j*j]+1)
        j += 1
print(dp[n])