# 순위 검색
from collections import defaultdict
from itertools import combinations
import bisect
def solution(info, query):
    check = defaultdict(list)
    answer = []
    for i, item in enumerate(info):
        l, w, y, f, s = item.split()
        for j in range(0, 5):
            key = list(combinations([l,w,y,f], j))
            for k in key:
                check[''.join(k)].append(int(s))
    for i in check:
        check[i].sort()
    for q in query:
        key, score = q.replace(' and ', '').split()
        key = key.replace('-','')
        answer.append(len(check[key]) - bisect.bisect_left(check[key], int(score)))
    return answer
solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])
# solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])