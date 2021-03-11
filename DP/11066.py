import sys
input = sys.stdin.readline
def dfs(i, j):
    if dp[i][j] != float('inf'): return dp[i][j]
    if i == j:
        dp[i][j] = 0
        return 0
    if j - i == 1:
        dp[i][j] = arr[i] + arr[j]
        return dp[i][j]
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], dfs(i, k) + dfs(k + 1, j))
    dp[i][j] += sumarr[j + 1] - sumarr[i]
    return dp[i][j]

T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0]*n for _ in range(n)]
    sumarr = [0]*(n+1)
    sumarr[1] = arr[0]
    for i in range(2, n+1):
        sumarr[i] = sumarr[i-1]+arr[i-1]
    # print(dfs(0, n-1))
    for x in range(1, n+1):
        for i in range(n-x):
            j = i+x
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
            dp[i][j] += sumarr[j+1] - sumarr[i]
    print(dp[0][n-1])
