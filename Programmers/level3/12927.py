import heapq
def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
    while n > 0:
        x = heapq.heappop(works)
        if x == 0: return 0
        heapq.heappush(works, x + 1)
        n -= 1
    answer = 0
    for work in works:
        answer += work*work
    return answer
