# 외벽 점검
from itertools import permutations
def solution(n, weak, dist_):
    answer = float('inf')
    # 점검할 외벽의 순열을 구하자
    m = len(weak)
    weak.sort()
    weaks = []
    for i in range(len(weak)):
        temp = []
        temp.extend(weak[i:])
        for j in range(i):
            temp.append(weak[j]+n)
        weaks.append(temp)
    for dist in list(permutations(dist_, len(dist_))):
        for w in weaks:
            friend = 0
            start = w[0]
            cnt = 1
            for i in range(1, m):
                if w[i] > start+dist[friend]:
                    friend += 1
                    if friend >= len(dist):
                        break
                    start = w[i]
                    cnt += 1
                else:
                    cnt += 1
            else:
                answer = min(answer, friend+1)
    if answer == float('inf'):
        return -1

    return answer
print(solution(12,	[1, 5, 6, 10],	[1, 2,3,4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))