from collections import deque

def solution(board):
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n = len(board)
    dp = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append([0, 0, 1])
    queue.append([0, 0, 2])
    dp[0][0][1] = 0
    dp[0][0][2] = 0

    while queue:
        x, y, d = queue.popleft()
        # 커브
        for i in [1, -1]:
            nd = (d + i) % 4
            cx, cy = x + move[nd][0], y + move[nd][1]
            if 0 <= cx < n and 0 <= cy < n and board[cx][cy] == 0 and dp[cx][cy][nd] > dp[x][y][d] + 6:
                dp[cx][cy][nd] = dp[x][y][d] + 6
                queue.append([cx, cy, nd])
        # 직진
        cx, cy = x + move[d][0], y + move[d][1]
        if 0 <= cx < n and 0 <= cy < n and board[cx][cy] == 0 and dp[cx][cy][d] > dp[x][y][d] + 1:
            dp[cx][cy][d] = dp[x][y][d] + 1
            queue.append([cx, cy, d])
    return min(dp[n - 1][n - 1]) * 100


# solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
