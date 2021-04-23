from copy import deepcopy
move = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
def fish_move(sx,sy):
    # print(sx, sy, board[sx][sy])
    for i in range(1, 17):
        if not fish[i]: continue
        x,y,d = fish[i]
        cx = x+move[d][0]
        cy = y+move[d][1]
        while not (0<=cx<4 and 0<=cy<4) or (cx==sx and cy==sy):
            d = (d+9)%8
            cx = x+move[d][0]
            cy = y+move[d][1]
            continue
        if board[cx][cy]:
            before = board[cx][cy]
            fish[before] = [x, y, fish[before][2]]
            fish[i] = [cx, cy, d]
            board[cx][cy] = i
            board[x][y] = before
        else:
            fish[i] = [cx, cy, d]
            board[cx][cy] = i
            board[x][y] = 0
def shark_move(sx, sy, d, ans):
    global answer, fish, board
    fish_move(sx, sy)
    fish_x = deepcopy(fish)
    board_x = deepcopy(board)
    for i in range(1, 4):
        cx, cy = sx+move[d][0]*i, sy+move[d][1]*i
        if not (0<=cx<4 and 0<=cy<4):
            answer = max(ans, answer)
            return
        if not board[cx][cy] : continue
        # 먹어!
        eat = board[cx][cy]
        d_x = fish[eat][2]
        fish[eat] = 0
        board[cx][cy] = 0
        shark_move(cx,cy,d_x,ans+eat)
        fish, board = fish_x, board_x

board = [[0]*4 for _ in range(4)]
fish = [[] for _ in range(17)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0,7,2):
        board[i][j//2] = temp[j]
        fish[temp[j]] = [i, j//2, temp[j+1]-1]

first_eat = board[0][0]
first_dir = fish[first_eat][2]
fish[first_eat] = 0
board[0][0] = 0
answer = 0
shark_move(0,0,first_dir,first_eat)
print(answer)
