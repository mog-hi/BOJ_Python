import heapq
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])
answer = 1
queue = []
heapq.heappush(queue, arr[0][1])
for start, end in arr[1:]:
    last = heapq.heappop(queue)
    if last > start:
        answer += 1
        heapq.heappush(queue, last)
    heapq.heappush(queue, end)
print(answer)
