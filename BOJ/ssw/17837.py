n, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
horse = []
horse_pos = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    r, c, d = map(int, input().split())
    horse.append([r-1, c-1, d-1])
    horse_pos[r-1][c-1].append(i)
move = [(0,1),(0,-1),(-1,0),(1,0)]
change_dir = [1,0,3,2]

for t in range(0, 1000):
    r, c = horse[0][0], horse[0][1]
    for i in range(k):
        r, c, d = horse[i]
        cr, cc = r+move[d][0], c+move[d][1]
        if (not (0<=cr<n and 0<=cc<n)) or board[cr][cc] == 2:
            horse[i][2] = change_dir[d]
            r, c, d = horse[i]
            cr, cc = r + move[d][0], c + move[d][1]
            if (not (0 <= cr < n and 0 <= cc < n)) or board[cr][cc] == 2: continue
        if board[cr][cc] == 0:
            idx = horse_pos[r][c].index(i)
            temp = horse_pos[r][c][idx:]
            for j in horse_pos[r][c][idx:]:
                horse[j][0] = cr
                horse[j][1] = cc
        elif board[cr][cc] == 1:
            idx = horse_pos[r][c].index(i)
            temp = horse_pos[r][c][idx:]
            for j in temp:
                horse[j][0] = cr
                horse[j][1] = cc
            temp.reverse()
        horse_pos[cr][cc].extend(temp)
        horse_pos[r][c] = horse_pos[r][c][:idx]
        if len(horse_pos[cr][cc]) >= 4:
            print(t+1)
            exit(0)
else:
    print(-1)
