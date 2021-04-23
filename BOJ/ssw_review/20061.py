def remove_green(x):
    for i in range(x, 0, -1):
        for j in range(4):
            green[i][j] = green[i-1][j]
    for j in range(4):
        green[0][j] = 0

def remove_blue(x):
    for j in range(x, 0, -1):
        for i in range(4):
            blue[i][j] = blue[i][j-1]
    for i in range(4):
        blue[i][0] = 0

n = int(input())
green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]
answer = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    # green
    for j in range(6):
        if t == 1:
            if green[j][y]:
                green[j-1][y] = 1
                break
        elif t == 2:
            if green[j][y] or green[j][y+1]:
                green[j-1][y] = 1
                green[j-1][y+1] = 1
                break
        else:
            if green[j][y]:
                green[j-1][y] = 1
                green[j-2][y] = 1
                break
    else:
        green[5][y] = 1
        if t == 2:
            green[5][y+1] = 1
        elif t == 3:
            green[4][y] = 1

    # blue
    for j in range(6):
        if t == 1:
            if blue[x][j]:
                blue[x][j-1] = 1
                break
        elif t == 2:
            if blue[x][j]:
                blue[x][j-1] = 1
                blue[x][j-2] = 1
                break
        else:
            if blue[x][j] or blue[x+1][j]:
                blue[x][j-1] = 1
                blue[x+1][j-1] = 1
                break
    else:
        blue[x][5] = 1
        if t == 2:
            blue[x][4] = 1
        elif t == 3:
            blue[x+1][5] = 1

    # 채워진 열/행
    for i in range(6):
        check = True
        for j in range(4):
            if green[i][j] == 0:
                check = False
                break
        if check:
            answer+=1
            remove_green(i)
        check = True
        for j in range(4):
            if blue[j][i] == 0:
                check = False
                break
        if check:
            answer+=1
            remove_blue(i)

    # 연한 부분
    for i in range(2):
        for j in range(4):
            if blue[j][i] == 1:
                remove_blue(5)
                break
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                remove_green(5)
                break
cnt = 0
for i in range(6):
    for j in range(4):
        if green[i][j] == 1:
            cnt += 1
        if blue[j][i] == 1:
            cnt += 1
print(answer)
print(cnt)

