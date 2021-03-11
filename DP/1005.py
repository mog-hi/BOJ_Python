# 30분
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    time = [0]
    time.extend(list(map(int, input().split())))
    graph = [[] for _ in range(n+1)]
    depth = [0]*(n+1)
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        depth[b] += 1
    w = int(input())
    queue = deque()
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if depth[i] == 0:
            queue.append(i)
            dp[i] = time[i]
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            depth[i] -= 1
            dp[i] = max(dp[i], dp[temp] + time[i])
            if depth[i] == 0:
                queue.append(i)
    print(dp[w])