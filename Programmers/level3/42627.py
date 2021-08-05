import heapq
def solution(jobs):
    answer = 0
    n = len(jobs)
    time = 0
    jobs.sort()
    while jobs:
        hq = []
        for start, length in jobs:
            if start <= time:
                heapq.heappush(hq, [length, start])
        if hq:
            temp = heapq.heappop(hq)
            print((time - temp[1]) + temp[0])
            answer += (time - temp[1]) + temp[0]
            time += temp[0]
            print(time)
            jobs.remove([temp[1], temp[0]])
        else:
            time += 1

    return answer//n
def solution2(jobs):
    answer = 0
    n = len(jobs)
    time = 0
    jobs.sort()
    while jobs:
        hq = []
        for start, length in jobs:
            if start <= time:
                heapq.heappush(hq, [length, start])
        if hq:
            temp = heapq.heappop(hq)
            answer += (time - temp[1]) + temp[0]
            time += temp[0]
            jobs.remove([temp[1], temp[0]])
        else:
            answer += jobs[0][1]
            time += (jobs[0][0] - time) + jobs[0][1]
            jobs.pop(0)
    return answer //n

print(solution([[1,3],[5,1], [5,5], [5,3], [5,1]]))
print('---------')
print(solution2([[1,3],[5,1], [5,5], [5,3], [5,1]]))

# print(solution([[0, 3], [1, 9], [2, 6]]))               # 9
# print(solution([[0, 3], [4, 3], [10, 3]]))              # 3
# print(solution([[0, 10], [2, 3], [9, 3]]))              # 9
# print(solution([[1, 10], [3, 3], [10, 3]]))             # 9
# print(solution([[0, 10]]))                              # 10
# print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))   # 15
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))   # 74
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74