# 10분
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
white = 0
blue = 0
def divide(size, x, y):
    global white, blue
    if size == 1:
        if board[x][y] == 1: blue += 1
        else: white += 1
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
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
        return
    divide(size//2, x, y)
    divide(size//2, x+size//2, y)
    divide(size//2, x, y+size//2)
    divide(size//2, x+size//2, y+size//2)
divide(n, 0, 0)
print(white)
print(blue)