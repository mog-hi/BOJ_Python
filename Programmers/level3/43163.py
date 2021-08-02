# 단어 변환
from collections import deque, defaultdict


def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = defaultdict(bool)

    while queue:
        temp, cnt = queue.popleft()
        if visited[temp]: continue
        visited[temp] = True
        if temp == target:
            return cnt
        for word in words:
            different = 0
            for i in range(len(word)):
                if word[i] != temp[i]:
                    different += 1
                    if different > 1: break
            else:
                queue.append([word, cnt + 1])
    return 0
