dice = [1, 3, 4, 5, 2, 6]
dicenum = [0] * 7
def rollDice(dir):
    if dir == 1:
        dice[0], dice[1], dice[2], dice[5] = dice[2], dice[0], dice[5], dice[1]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[5] = dice[1], dice[5], dice[0], dice[2]
    elif dir == 3:
        dice[0], dice[3], dice[4], dice[5] = dice[3], dice[5], dice[0], dice[4]
    elif dir == 4:
        dice[0], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[3]

n, m, x, y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
move = list(map(int, input().split()))
xydir = [(0,1), (0,-1), (-1,0), (1,0)]
for i in move:
    cx = x + xydir[i-1][0]
    cy = y + xydir[i-1][1]
    if cx < 0 or cx >= n or cy < 0 or cy >= m:
        continue
    rollDice(i)
    if board[cx][cy] == 0:
        board[cx][cy] = dicenum[dice[5]]
    else:
        dicenum[dice[5]] = board[cx][cy]
        board[cx][cy] = 0
    print(dicenum[dice[0]])
    x, y = cx, cy