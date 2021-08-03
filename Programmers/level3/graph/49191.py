# 순위

def solution(n, results):
    win = [set() for _ in range(n)]
    lose = [set() for _ in range(n)]
    for a, b in results:
        a, b = a - 1, b - 1
        win[a].add(b)
        lose[b].add(a)

    for a in range(n):
        for b in lose[a]:
            win[b].update(win[a])
        for b in win[a]:
            lose[b].update(lose[a])
    answer = 0
    for i in range(n):
        if len(set(win[i])) + len(set(lose[i])) == n-1:
            answer += 1
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
solution(5, [[1, 4], [2, 3], [2, 5], [3, 5], [4, 5]])
