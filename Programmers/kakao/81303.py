from heapq import heappop, heappush
def solution(n, k, cmd):
    stack = []
    minHeap = []
    maxHeap = []
    for i in range(k+1):
        heappush(minHeap, -i)
    for i in range(k+1, n):
        heappush(maxHeap, i)
    for i in cmd:
        if i == 'C':
            stack.append(-heappop(minHeap))
            if maxHeap:
                heappush(minHeap, -heappop(maxHeap))
            continue
        if i == 'Z':
            x = stack.pop()
            pointer = -heappop(minHeap)
            if x < pointer:
                heappush(minHeap, -x)
            else:
                heappush(maxHeap, x)
            heappush(minHeap, -pointer)
            continue
        direction, cnt = i.split()
        cnt = int(cnt)
        if direction == 'U':
            for i in range(cnt):
                x = heappop(minHeap)
                heappush(maxHeap, -x)
            continue
        if direction == 'D':
            for i in range(cnt):
                x = heappop(maxHeap)
                heappush(minHeap, -x)
            continue
    answer = ['X']*n
    for i in minHeap:
        i = -i
        answer[i] = 'O'
    for i in maxHeap:
        answer[i] = 'O'
    return ''.join(answer)


# solution(8,2,["D 2"])
# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
