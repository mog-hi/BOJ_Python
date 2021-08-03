# 네트워크
from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    queue = deque()
    for i in range(n):
        if visited[i]: continue
        answer += 1
        queue.append(i)
        while queue:
            temp = queue.popleft()
            if visited[temp]: continue
            visited[temp] = 1
            for j in range(n):
                if computers[temp][j]:
                    queue.append(j)
    print(answer)

    return answer