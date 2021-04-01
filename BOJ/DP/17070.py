# dfs로 하다가 시간 초과.. 40분 걸림
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if j + 1 < n and board[i][j + 1] != 1:
            dp[i][j+1][0] += dp[i][j][0] + dp[i][j][2]
        if i+1 < n and board[i+1][j] != 1:
            dp[i+1][j][1] += dp[i][j][1] + dp[i][j][2]
        if i+1 < n and j+1 < n and board[i+1][j+1] != 1 and board[i+1][j] != 1 and board[i][j+1] != 1:
            dp[i+1][j+1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
print(sum(dp[n-1][n-1]))