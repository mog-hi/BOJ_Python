from collections import deque


def check(start, end):
    if start[0] == end[0]:
        return 1  # 가로
    elif start[1] == end[1]:
        return 0  # 세로


def solution(board):
    n = len(board)
    answer = float('inf')
    robot = [[0, 0], [0, 1]]
    queue = deque()
    visited = [[0] * (n * n) for _ in range(n * n)]
    queue.append([robot, 0])
    while queue:
        [left, right], cnt = queue.popleft()
        if left == [n-1, n-1] or right == [n-1,n-1]:
            answer = min(answer, cnt)
            continue
        x, y = left
        a, b = right
        if visited[x*n+y][a*n+b]:
            continue
        visited[x * n + y][a * n + b] = 1
        # 이동
        for j in [1, -1]:
            cy = j + y
            cb = j + b
            if 0 <= cy < n and board[x][cy] == 0 and 0 <= cb < n and board[a][cb] == 0:
                queue.append([[[x, cy], [a, cb]], cnt + 1])

        for j in [1, -1]:
            cx = j + x
            ca = j + a
            if 0 <= cx < n and board[cx][y] == 0 and 0 <= ca < n and board[ca][b] == 0:
                queue.append([[[cx, y], [ca, b]], cnt + 1])

        # 회전
        if check(left, right):  # 가로
            # x, y 기준
            for j in [1, -1]:
                ca, cb = x+j, y
                if 0 <= ca < n and 0 <= cb < n and board[ca][cb] == 0 and board[ca][b] == 0:
                    queue.append([[[x, y], [ca, cb]], cnt+1])
            # a, b 기준
            for j in [1, -1]:
                cx, cy = a+j, b
                if 0 <= cx < n and 0 <= cy < n and board[cx][cy] == 0 and board[cx][y] == 0:
                    queue.append([[[cx, cy], [a, b]], cnt+1])
        else:
            # x, y 기준
            for j in [1, -1]:
                ca, cb = x, y+j
                if 0 <= ca < n and 0 <= cb < n and board[ca][cb] == 0 and board[a][cb] == 0:
                    queue.append([[[x, y], [ca, cb]], cnt+1])
            # a, b 기준
            for j in [1, -1]:
                cx, cy = a, b+j
                if 0 <= cx < n and 0 <= cy < n and board[cx][cy] == 0 and board[x][cy] == 0:
                    queue.append([[[cx, cy], [a, b]], cnt+1])

    return answer
solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])