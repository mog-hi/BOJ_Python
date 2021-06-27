# LCS
a = ' ' + input()
b = ' ' + input()
n = len(a)
m = len(b)
dp = [[0]*m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(max(dp[n-1]))