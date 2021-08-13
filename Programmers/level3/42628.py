def solution(operations):
    arr = []
    for op in operations:
        if op[0] == 'I':
            arr.append(int(op[2:]))
            arr.sort()
            continue
        if not arr: continue
        if op == 'D 1':
            arr.pop()
        elif op == 'D -1':
            arr.pop(0)
    if not arr:
        return [0, 0]
    return [max(arr), min(arr)]

import heapq
heap = [1,4,2,1,8,4,5]
heapq.heapify(heap)
print(heapq.heappop(heap))
print(heapq.nlargest(4, heap))