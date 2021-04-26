from itertools import combinations
from copy import deepcopy
n, m, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
ans = 0
for arr in list(combinations(range(0, m), 3)):
    board_x = deepcopy(board)
    # 공격
    answer = 0
    for x in range(n, 0, -1):
        delete = []
        for y in arr:
            where = []
            for i in range(x-1, -1, -1):
                for j in range(m):
                    if not board[i][j]: continue
                    distance = abs(x-i) + abs(y-j)
                    if distance <= d:
                        where.append((distance,i, j))
            where.sort(key=lambda x:[x[0], x[2]])
            if where:
                delete.append(where[0][1:])
        for i, j in delete:
            if board[i][j]:
                answer+=1
                board[i][j] = 0
    ans = max(ans, answer)
    board = board_x
print(ans)