from copy import deepcopy
R,C,M = map(int, input().split())
exist = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    exist[r-1][c-1] = [s, d-1, z]
move = [(-1,0), (1,0), (0,1),(0, -1)]
change_dir = [1,0,3,2]
def shark_move():
    global exist
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for a in range(R):
        for b in range(C):
            if len(exist[a][b]) == 0: continue
            s, d, z = exist[a][b]
            x, y = a, b
            for j in range(s):
                x += move[d][0]
                y += move[d][1]
                if not (0 <= x < R and 0 <= y < C):
                    x -= move[d][0]
                    y -= move[d][1]
                    d = change_dir[d]
                    x, y = x + move[d][0], y + move[d][1]
            if temp[x][y] and temp[x][y][2] > z: continue
            temp[x][y] = [s, d, z]
    exist = temp
answer = 0
for i in range(C):
    for j in range(R):
        if exist[j][i]:
            answer += exist[j][i][2]
            exist[j][i] = []
            break
    shark_move()
print(answer)
