from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for i in course:
        cnt = defaultdict(int)
        for s in orders:
            for j in list(combinations(s, i)):
                j = sorted(j)
                cnt[''.join(j)] += 1
        arr = list(cnt.items())
        arr.sort(key=lambda x:[-x[1],x[0]])
        max_cnt = 0
        for key, cnt in arr:
            if max_cnt > cnt or cnt < 2: break
            max_cnt = cnt
            answer.append(key)
    answer.sort()
    return answer
solution(["XYZ", "XWY", "WXA"], [2,3,4])
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])