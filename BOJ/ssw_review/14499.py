n, m, x, y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
dice = [0]*6
arr = list(map(int, input().split()))

def play(d):
    if d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif d == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
for i in arr:
    if 0<=x+move[i][0]<n and 0<=y+move[i][1]<m:
        x += move[i][0]
        y += move[i][1]
        play(i)
        print(dice[0])
        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0