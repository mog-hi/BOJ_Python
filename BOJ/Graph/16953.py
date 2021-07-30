from collections import defaultdict
import heapq
a, b = map(int, input().split())
queue = []
visited = defaultdict(bool)
heapq.heappush(queue, [1, a])
while queue:
    cnt, temp = heapq.heappop(queue)
    if temp == b:
        print(cnt)
        break
    if temp > b:
        continue
    if visited[temp]:
        continue
    visited[temp] = True
    heapq.heappush(queue, [cnt+1, temp*2])
    heapq.heappush(queue, [cnt+1, temp*10+1])
else:
    print(-1)