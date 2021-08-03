# 가장 먼 노드
import heapq
def solution(n, edge):
    graph = [[] for _ in range(n)]
    for a, b in edge:
        a, b = a-1, b-1
        graph[a].append(b)
        graph[b].append(a)
    distance = [float('inf')]*n
    queue = []
    heapq.heappush(queue, 0)
    distance[0] = 0
    while queue:
        temp = heapq.heappop(queue)
        for node in graph[temp]:
            if distance[node] > distance[temp] + 1:
                distance[node] = distance[temp] + 1
                heapq.heappush(queue, node)
    maxDistance = max(distance)
    answer = 0
    for i in range(n):
        if distance[i] == maxDistance:
            answer += 1
    return answer

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])