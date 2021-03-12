n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
answer = [0, 0, 0]
arr = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
def divide(size, x, y):
    global answer
    if size == 1:
        answer[board[x][y]+1] += 1
        return
    last = board[x][y]
    allSame = True
    for i in range(x, x+size):
        if not allSame: break
        for j in range(y, y+size):
            if last != board[i][j]:
                allSame = False
                break
    if allSame:
        answer[board[x][y]+1] += 1
        return
    for i, j in arr:
        divide(size//3, x+i*(size//3), y+j*(size//3))
divide(n, 0, 0)
for i in answer:
    print(i)