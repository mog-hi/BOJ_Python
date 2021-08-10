from collections import deque
def solution(n, costs):
    graph = [[-1]*n for _ in range(n)]

    def bfs():
        visited = [0]*n
        queue = deque()
        queue.append(0)
        while queue:
            temp = queue.popleft()
            if visited[temp]: continue
            visited[temp] = 1
            for i in range(n):
                if graph[temp][i] != -1:
                    queue.append(i)
        for i in visited:
            if i == 0: return False
        return True

    answer = 0
    for i, j, cost in costs:
        graph[i][j] = cost
        graph[j][i] = cost
        answer += cost
    costs.sort(key=lambda x: -x[2])

    for i, j, cost in costs:
        graph[i][j] = -1
        graph[j][i] = -1
        if not bfs():
            graph[i][j] = cost
            graph[j][i] = cost
        else:
            answer -= cost
    return answer
