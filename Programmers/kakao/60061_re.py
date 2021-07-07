N = 0
board = []
result = []

def build(x, y, i):
    if i == 0:
        if (x > 0 and board[y][x - 1][1]) or board[y][x][1]:
            return True
        if y == 0:
            return True
        if y > 0 and board[y - 1][x][0]:
            return True
    elif i == 1:
        if (y > 0 and board[y - 1][x][0]) or (y > 0 and x < N and board[y - 1][x + 1][0]):
            return True
        if (x > 0 and board[y][x - 1][1]) and (x < N and board[y][x + 1][1]):
            return True
    return False

def check():
    for x, y, i in result:
        if not build(x,y,i):
            return False
    return True

def solution(n, build_frame):
    global N, board
    N = n
    board = [[[0, 0] for _ in range(N + 1)] for _ in range(N + 1)]
    for x, y, i, j in build_frame:
        if j == 1:
            if build(x, y, i):
                result.append([x, y, i])
                board[y][x][i] = 1
        elif j == 0:
            board[y][x][i] = 0
            result.remove([x, y, i])
            if not check():
                board[y][x][i] = 1
                result.append([x, y, i])
    result.sort()
    return result


# solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
#              [3, 2, 1, 1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])