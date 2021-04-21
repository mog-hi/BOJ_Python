n = int(input())
arr = []
total = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
    total+=sum(arr[i])
answer = total
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if not (x+d1+d2<n and 0<=y-d1 and y+d2<n): continue
                board = [[0]*n for _ in range(n)]
                for i in range(d1+1):
                    board[x+i][y-i] = 1
                    board[x+d2+i][y+d2-i] = 1
                for i in range(d2+1):
                    board[x+i][y+i] = 1
                    board[x+d1+i][y-d1+i] = 1
                res = [0]*5
                # 0
                for i in range(x+d1):
                    for j in range(y+1):
                        if board[i][j] == 1:
                            break
                        res[0] += arr[i][j]
                # 1
                for i in range(x+d2+1):
                    for j in range(n-1, y, -1):
                        if board[i][j] == 1:
                            break
                        res[1] += arr[i][j]
                # 2
                for i in range(x+d1, n):
                    for j in range(y-d1+d2):
                        if board[i][j] == 1:
                            break
                        res[2] += arr[i][j]
                # 3
                for i in range(x+d2+1, n):
                    for j in range(n-1, y-d1+d2-1, -1):
                        if board[i][j] == 1:
                            break
                        res[3] += arr[i][j]
                res[4] = total-sum(res[:4])
                answer = min(answer, max(res)-min(res))
print(answer)