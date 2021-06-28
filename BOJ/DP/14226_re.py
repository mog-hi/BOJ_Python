from collections import deque
n = int(input())
dp = [[float('inf')]*(n+1) for _ in range(n+1)]
queue = deque()
queue.append([1, 0])
dp[1][0] = 0
while queue:
    x, y = queue.popleft()
    if dp[x][x]>dp[x][y]+1:
        dp[x][x] = dp[x][y]+1
        queue.append([x, x])
    if x+y <= n and dp[x+y][y]>dp[x][y]+1:
        dp[x+y][y] = dp[x][y]+1
        queue.append([x+y, y])
    if 0<=x-1 and dp[x-1][y]>dp[x][y]+1:
        dp[x-1][y] = dp[x][y]+1
        queue.append([x-1, y])
print(min(dp[n]))