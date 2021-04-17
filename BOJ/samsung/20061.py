green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]

def block_move(t, x, y):
    # green에서 자리 찾기
    green_x = 5
    for i in range(6):
        if (t == 2 and (green[i][y] == 1 or green[i][y+1] == 1)) or (t!=2 and green[i][y] == 1):
            green_x = i-1
            break

    # blue에서 자리 찾기
    blue_y = 5
    for i in range(6):
        if (t==3 and (blue[x][i] == 1 or blue[x+1][i] == 1)) or (t!=3 and blue[x][i] == 1):
            blue_y = i-1
            break

    green[green_x][y] = 1
    blue[x][blue_y] = 1
    if t == 2:
        green[green_x][y + 1] = 1
        blue[x][blue_y - 1] = 1
    elif t == 3:
        green[(green_x - 1)][y] = 1
        blue[x+1][blue_y] = 1

def special_block():
    global green, blue
    green_cnt, blue_cnt = 0, 0

    if sum(green[1]) != 0:
        green_cnt = 1
    if sum(green[0]) != 0:
        green_cnt = 2
    for i in range(4):
        if blue[i][0] == 1:
            blue_cnt = 2
            break
        if blue[i][1] == 1:
            blue_cnt = 1

    # 연한 부분 조정
    if green_cnt > 0:
        new_green = [[0] * 4 for _ in range(6)]
        if green_cnt == 1:
            new_green[2:] = green[1:5]
        elif green_cnt == 2:
            new_green[2:] = green[:4]
        green = new_green
    if blue_cnt > 0:
        new_blue = [[0] * 6 for _ in range(4)]
        for j in range(5, 1, -1):
            for i in range(4):
                new_blue[i][j] = blue[i][j - blue_cnt]
        blue = new_blue

def delete_full():
    cnt = 0
    # green
    # 나는 맨 아래 부터 검사해서 끌어 내리는거로 생각해봤는데 위에서 부터 해도 똑같다.
    for i in range(2, 6):
        if sum(green[i]) == 4:
            cnt += 1
            for k in range(i, 0, -1):
                for j in range(4):
                    green[k][j] = green[k - 1][j]
            for j in range(4):
                green[0][j] = 0
    # i = 5
    # while i > 0:
    #     if sum(green[i]) == 4:
    #         cnt += 1
    #         for k in range(i, 0, -1):
    #             for j in range(4):
    #                 green[k][j] = green[k - 1][j]
    #         for j in range(4):
    #             green[0][j] = 0
    #     else:
    #         i -= 1

    # blue
    for j in range(2, 6):
        if blue[0][j] == blue[1][j] == blue[2][j] == blue[3][j] == 1:
            cnt += 1
            for k in range(j, 0, -1):
                for i in range(4):
                    blue[i][k] = blue[i][k - 1]
            for i in range(4):
                blue[i][0] = 0
    # j = 5
    # while j > 0:
    #     if blue[0][j] == blue[1][j] == blue[2][j] == blue[3][j] == 1:
    #         cnt += 1
    #         for k in range(j, 0, -1):
    #             for i in range(4):
    #                 blue[i][k] = blue[i][k - 1]
    #         for i in range(4):
    #             blue[i][0] = 0
    #     else:
    #         j -= 1
    return cnt

n = int(input())
answer = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    block_move(t, x, y)
    answer += delete_full()
    special_block()
cnt = 0
for i in range(4):
    for j in range(6):
        if blue[i][j] == 1:
            cnt += 1
        if green[j][i] == 1:
            cnt += 1
print(answer)
print(cnt)
