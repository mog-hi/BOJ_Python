n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
def bfs(start):
    queue = []
    queue.append(start)
    visited = [False]*n
    while queue:
        temp = queue.pop()
        for i in range(n):
            if graph[temp][i]:
                graph[start][i] = 1
                if visited[i]: continue
                visited[i] = True
                queue.append(i)
for i in range(n):
    bfs(i)
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()