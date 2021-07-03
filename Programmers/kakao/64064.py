# 불량사용자
from collections import deque
from copy import deepcopy
from itertools import product


def check(a, b):
    if len(a) != len(b): return False
    for i in range(len(a)):
        if not (a[i] == b[i] or b[i] == '*'):
            return False
    return True


def solution2(user_id, banned_id):
    graph = [[] for _ in range(len(banned_id))]
    for ban_idx, ban in enumerate(banned_id):
        for user in user_id:
            if check(user, ban):
                graph[ban_idx].append(user)
    candidate = list(product(*graph))
    # 다른 인덱스에 같은 원소 들어간거 제거 + 순서만 다른 같은 조합 제거
    result = []
    for i in candidate:
        if len(set(i)) == len(banned_id):
            temp = sorted(i)
            if temp not in result:
                result.append(temp)
    return len(result)


def solution(user_id, banned_id):
    graph = [[] for _ in range(len(banned_id))]
    for ban_idx, ban in enumerate(banned_id):
        for user_idx, user in enumerate(user_id):
            if check(user, ban):
                graph[ban_idx].append(user_idx)
    # bfs
    queue = deque()
    for i in graph[0]:
        visited = [0] * len(user_id)
        visited[i] = 1
        queue.append([0, visited])
    result = []
    while queue:
        temp, visited = queue.popleft()
        if temp >= len(banned_id) - 1:
            if visited not in result:
                result.append(visited)
            continue
        for i in graph[temp + 1]:
            if not visited[i]:
                temp_visited = deepcopy(visited)
                temp_visited[i] = 1
                queue.append([temp + 1, temp_visited])
    return len(result)


# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution2(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
