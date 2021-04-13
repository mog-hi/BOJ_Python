# 외벽 점검
import heapq
from itertools import permutations

def solution(n, weak, dist):
    m = len(weak)
    # 그래프처럼 탐색하기 위해 이차원 배열 graph 생성
    graph = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            temp = min((weak[i]-weak[j]+n)%n, (weak[j]-weak[i]+n)%n)
            graph[i][j] = temp
            graph[j][i] = temp

    answer = float('inf')
    per = list(permutations(dist, len(dist))) # dist에 대한 모든 순열 탐색
    for k in range(len(per)):
        queue = []
        x = 0
        visited = [0]*m
        heapq.heappush(queue, (0, 0))
        i = 0
        dist_ = per[k]
        while queue:
            c, temp = heapq.heappop(queue)
            if visited[temp]: continue
            visited[temp] = 1
            if x + c > dist_[i]:
                i += 1  # 다음 친구에게 넘겨주기
                x = 0
            else:
                x += c
            if i > len(dist) -1:
                break # 마지막 친구까지 했는데 못했을 때 -> 해당 dist에서 취약 지점을 전부 점검할 수 없는 경우
            for j in range(m):
                heapq.heappush(queue, (graph[temp][j], j))
        else:
            answer = min(answer, i+1)
    if answer == float('inf'):
        return -1
    return answer

print(solution(12,	[1, 5, 6, 10],	[1, 2,3,4]))
print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
# print(list(permutations([1,2,3,4], 4)))