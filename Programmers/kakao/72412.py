# 순위 검색
from itertools import combinations
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    people = defaultdict(list)
    for i in info:
        person = i.split()
        score = int(person[-1])
        people[''.join(person[:-1])].append(score)
        for j in range(4):
            candi = list(combinations(person[:-1], j))
            for c in candi:
                people[''.join(c)].append(score)
    print(people)
    for i in people:
        people[i].sort()
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key])-bisect.bisect_left(people[key], score))
    return answer
solution(	["java backend junior pizza 150"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])