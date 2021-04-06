n = int(input())
board = [[0] * 101 for i in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(n):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1
    arr = [d]
    q = [d]
    for i in range(g+1):
        for j in q:
            x += dx[j]
            y += dy[j]
            board[x][y] = 1
        q = [(k+1) % 4 for k in arr]
        q.reverse()
        arr = arr + q
result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
            result += 1
print(result)
