from collections import deque
s = int(input())
dp = [[-1]*(s+1) for _ in range(s+1)]
queue = deque()
queue.append((1, 0))
dp[1][0] = 0
while queue:
    x, y = queue.popleft()
    if dp[x][x] == -1:
        dp[x][x] = dp[x][y] + 1
        queue.append((x, x))
    if x + y <= s and dp[x+y][y] == -1:
        dp[x+y][y] = dp[x][y] + 1
        queue.append((x+y, y))
    if x - 1 >= 0 and dp[x-1][y] == -1:
        dp[x-1][y] = dp[x][y] + 1
        queue.append((x-1, y))
answer = dp[s][1]
for i in range(2, s):
    if dp[s][i] != -1:
        answer = min(answer, dp[s][i])
print(answer)