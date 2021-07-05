from collections import defaultdict
from copy import deepcopy


def solution(stones, k):
    left = 0
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        temp = deepcopy(stones)
        for i in range(len(temp)):
            temp[i] -= mid
        cnt = 0
        for i in temp:
            if i <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        else:
            left = mid + 1
            continue
        right = mid - 1
    return right


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
