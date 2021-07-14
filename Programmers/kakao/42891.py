import heapq


def solution(food_times, k):
    queue = [[food_time, i + 1] for i, food_time in enumerate(food_times)]
    heapq.heapify(queue)
    pre_time = 0
    time = 0
    while queue:
        food_time = queue[0][0]
        length = len(queue)
        time += (food_time - pre_time) * length
        if time > k:
            time -= (food_time - pre_time) * length
            arr = []
            while queue:
                arr.append(heapq.heappop(queue)[1])
            arr.sort()
            answer = arr[(k - time) % length]
            return answer
        else:
            pre_time = heapq.heappop(queue)[0]
    return -1


solution([3, 1, 2], 5)
