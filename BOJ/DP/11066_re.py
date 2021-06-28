n = int(input())
arr = list(map(int, input().split()))
dp = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
def dfs(i, j):
    if i == j:
        return 0
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], dfs(i,k)+dfs(k+1,j)+sum(arr[i:k+1])+sum(arr[k+1:j+1]))
    return dp[i][j]
dfs(0, n-1)
print(dp[0][n-1])