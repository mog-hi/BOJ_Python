n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))
answer = float('inf')
def backtracking(loc, arr):
    global answer
    if len(arr) == m:
        townChickenDis = 0
        for i, j in home:
            chickenDis = float('inf')
            for x, y in arr:
                chickenDis = min(chickenDis, abs(i-x)+abs(j-y))
            townChickenDis += chickenDis
        answer = min(answer, townChickenDis)
        return
    if loc >= len(chicken): return
    for i in range(loc, len(chicken)):
        arr.append(chicken[i])
        backtracking(i+1, arr)
        arr.pop()
backtracking(0,[])
print(answer)


