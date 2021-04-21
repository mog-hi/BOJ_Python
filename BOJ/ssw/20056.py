n, m, k = map(int,input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])
move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(k):
    new_board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(len(board[i][j])):
                m, s, d = board[i][j][k]
                x, y = (i+s*move[d][0]+n)%n, (j+s*move[d][1]+n)%n
                new_board[x][y].append((m, s, d))
    board=new_board
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1:
                cnt = len(board[i][j])
                sum_m = 0
                sum_s = 0
                is_all = True
                last = board[i][j][0][2]
                for k in range(len(board[i][j])):
                    sum_m += board[i][j][k][0]
                    sum_s += board[i][j][k][1]
                    if is_all and last%2 == board[i][j][k][2]%2:
                        is_all = True
                    else:
                        is_all = False
                if sum_m//5 == 0:
                    temp = []
                else:
                    if is_all:
                        temp = [(sum_m//5, sum_s//cnt, 0), (sum_m//5, sum_s//cnt, 2), (sum_m//5, sum_s//cnt, 4), (sum_m//5, sum_s//cnt, 6)]
                    else:
                        temp = [(sum_m//5, sum_s//cnt, 1), (sum_m//5, sum_s//cnt, 3), (sum_m//5, sum_s//cnt, 5), (sum_m//5, sum_s//cnt, 7)]
                board[i][j] = temp
answer = 0
for i in range(n):
    for j in range(n):
        for k in range(len(board[i][j])):
            answer += board[i][j][k][0]
print(answer)