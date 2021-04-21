from copy import deepcopy

def fish_move(fish, fish_pos, r, c):
    f = deepcopy(fish)
    fp = deepcopy(fish_pos)
    for i in range(1, 17):
        if f[i][0] == -1: continue
        x, y, d = f[i]
        while (not (0<=x+move[d][0]<4 and 0<=y+move[d][1]<4)) or (x+move[d][0]==r and y+move[d][1] == c):
            d = (d+1)%8
        next_x = x+move[d][0]
        next_y = y+move[d][1]
        if fp[next_x][next_y] == 0:
            fp[x][y] = 0
        else:
            fp[x][y] = fp[next_x][next_y]
            f[fp[next_x][next_y]][0] = x
            f[fp[next_x][next_y]][1] = y
        fp[next_x][next_y] = i
        f[i] = [next_x, next_y, d]
    return f, fp

def backtraking(r, c, d, result, f, fp):
    global answer
    cango = False
    fish, fish_pos = fish_move(f, fp, r, c)
    for i in range(1, 4):
        cr = r + move[d][0] * i
        cc = c + move[d][1] * i
        if 0<=cr<4 and 0<=cc<4 and fish_pos[cr][cc] != 0:
            x = fish_pos[cr][cc]
            before = fish[x]
            fish[x] = [-1, -1, -1]
            fish_pos[cr][cc] = 0
            backtraking(cr, cc, before[2], result+x, fish, fish_pos)
            fish[x] = before
            fish_pos[cr][cc] = x
            cango = True
    if not cango:
        answer = max(answer, result)
        return
    return

fish = [[-1, -1, -1] for _ in range(17)]
fish_pos = [[0]*4 for _ in range(4)]
move = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        fish[temp[2*j]] = [i, j, temp[2*j+1]-1]
        fish_pos[i][j] = temp[2*j]
answer = 0

# 첫번째 물고기 잡아먹기
x = fish_pos[0][0]
d = fish[x][2]
fish[x] = [-1, -1, -1]
fish_pos[0][0] = 0
backtraking(0, 0, d, x, fish, fish_pos)
print(answer)