import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# visited = [False]*26
# answer = 0
# def dfs(x, y, cnt):
#     global answer
#     answer = max(answer, cnt)
#     for i, j in move:
#         cx = i+x
#         cy = j+y
#         if 0<=cx<n and 0<=cy<m:
#             k = ord(arr[cx][cy])-65
#             if not visited[k]:
#                 visited[k] = True
#                 dfs(cx, cy, cnt+1)
#                 visited[k] = False
#
# move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     arr.append(input())
# answer = 0
# visited[ord(arr[0][0])-65] = True
# dfs(0, 0, 1)
# print(answer)
def bfs():
    global answer
    visit = arr[0][0]
    queue = set([(0, 0, visit)])

    while queue:
        x, y, visited = queue.pop()
        answer = max(answer, len(visited))
        for i, j in move:
            cx = i+x
            cy = j+y
            if 0<=cx<n and 0<=cy<m:
                if arr[cx][cy] not in visited:
                    queue.add((cx, cy, visited+arr[cx][cy]))


move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
answer = 0
bfs()
print(answer)

