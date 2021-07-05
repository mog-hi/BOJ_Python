import heapq

graph = []


def dijkstra(start, n):
    global graph
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        dist, temp = heapq.heappop(queue)
        for i in range(1, n + 1):
            if distance[i] > dist + graph[temp][i]:
                distance[i] = dist + graph[temp][i]
                heapq.heappush(queue, [distance[i], i])
    return distance


def solution(n, s, a, b, fares):
    global graph
    answer = float('inf')
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i, j, cost in fares:
        graph[i][j] = cost
        graph[j][i] = cost

    for i in range(n + 1):
        sToI = dijkstra(s, n)[i]
        temp = dijkstra(i, n)
        answer = min(answer, sToI + temp[a] + temp[b])
    return answer


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
