from collections import defaultdict
from copy import deepcopy
from itertools import permutations
import heapq

board = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(start, end):
    x, y = start
    tox, toy = end
    queue = []
    heapq.heappush(queue, [0, x, y])
    visited = [[float('inf')] * 4 for _ in range(4)]
    visited[x][y] = 0
    while queue:
        cnt, r, c = heapq.heappop(queue)
        if r == tox and c == toy:
            return cnt
        # 인접
        for i, j in move:
            cr, cc = i + r, j + c
            if 0 <= cr < 4 and 0 <= cc < 4 and visited[cr][cc] > visited[r][c] + 1:
                visited[cr][cc] = visited[r][c] + 1
                heapq.heappush(queue, [visited[cr][cc], cr, cc])
        # ctrl
        for i, j in move:
            cr, cc = i + r, j + c
            while 0 <= cr < 4 and 0 <= cc < 4:
                if board[cr][cc]:
                    break
                cr += i
                cc += j
            else:
                cr -= i
                cc -= j
            if visited[cr][cc] > visited[r][c] + 1:
                visited[cr][cc] = visited[r][c] + 1
                heapq.heappush(queue, [visited[cr][cc], cr, cc])

def solution(b, x, y):
    global board
    arr = set()
    table = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if b[i][j]:
                arr.add(b[i][j])
                table[b[i][j]].append([i, j])
    permu = list(permutations(arr, len(arr)))
    answer = float('inf')
    for order in permu:
        r, c = x, y
        cost = 0
        board = deepcopy(b)
        for item in order:
            left = bfs([r, c], table[item][0]) + bfs(table[item][0], table[item][1])
            right = bfs([r, c], table[item][1]) + bfs(table[item][1], table[item][0])
            if left < right:
                cost += left + 2
                r, c = table[item][1]
            else:
                cost += right + 2
                r, c = table[item][0]
            board[table[item][0][0]][table[item][0][1]] = 0
            board[table[item][1][0]][table[item][1][1]] = 0
        answer = min(answer, cost)
    return answer


solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
