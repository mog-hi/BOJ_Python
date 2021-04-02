# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        temp = []
        for j in orders:
            temp.extend(list(combinations(sorted(j), i)))
        counter = Counter(temp)
        if not counter: continue
        m = max(counter.values())
        if m < 2: continue
        for i in counter.keys():
            if counter[i] == m:
                answer.append(''.join(i))
    answer.sort()
    return answer


solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
print(Counter(['abc', 'a', 'a', 'ab', 'ab', 'a']))