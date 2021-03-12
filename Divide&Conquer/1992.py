# 12분
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, list(input()))))
def divide(size, x, y):
    if size == 1:
        print(board[x][y], end='')
        return
    last = board[x][y]
    allSame = True
    for i in range(x , x+size):
        if not allSame: break
        for j in range(y, y+size):
            if last!= board[i][j]:
                allSame = False
                break
    if allSame:
        print(last, end='')
        return
    print('(', end='')
    divide(size//2,  x, y)
    divide(size//2,  x, y + size//2)
    divide(size//2,  x + size//2, y)
    divide(size//2,  x + size//2, y + size//2)
    print(')', end='')
divide(n, 0, 0)