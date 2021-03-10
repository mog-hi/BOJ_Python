from collections import deque
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
# result = 0
# def dfs(arr, total):
#     global result, cnt
#     if len(arr) == 4:
#         result = max(result, total)
#         return
#     for i in arr:
#         x = i//m
#         y = i % m
#         for r, k in move:
#             cx = r + x
#             cy = k + y
#             if 0<=cx<n and 0<=cy<m and cx*m+cy not in arr:
#                 arr.append(cx*m+cy)
#                 dfs(arr, total+board[cx][cy])
#                 arr.pop()
#
# for i in range(n):
#     for j in range(m):
#         dfs([i*m+j], board[i][j])
# print(result)
possible = [
    [[0,0],[0,1],[0,2],[0,3]], #-
    [[0,0],[1,0],[2,0],[3,0]], #ㅣ
    [[0,0],[0,1],[1,0],[1,1]], #ㅁ
    [[0,0],[0,1],[0,2],[1,0]], #ㄱ
    [[0,0],[0,1],[0,2],[1,2]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,2],[1,2],[1,1],[1,0]],
    [[0,1],[0,0],[1,0],[2,0]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[2,0],[2,1]],
    [[0,1],[1,1],[2,1],[2,0]],
    [[0,0],[0,1],[0,2],[1,1]], #ㅜ
    [[0,1],[1,0],[1,1],[1,2]],
    [[0,0],[1,0],[1,1],[2,0]],
    [[1,0],[0,1],[1,1],[2,1]],
    [[0,1],[1,1],[1,0],[2,0]],
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,1],[0,2],[1,1],[1,0]],
    [[0,0],[0,1],[1,1],[1,2]]
]
answer = 0
for i in range(n):
    for j in range(m):
        for s in possible:
            temp = 0
            for k in range(4):
                x = i + s[k][0]
                y = j + s[k][1]
                if 0<=x<n and 0<=y<m:
                    temp += board[x][y]
                else: break
            answer = max(answer , temp)
print(answer)
