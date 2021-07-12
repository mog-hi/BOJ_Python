from collections import deque


def bfs(x, y, place):
    queue = deque()
    visited = [[0] * 5 for _ in range(5)]
    queue.append((0, x, y))
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        cnt, x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        if cnt == 2:
            break
        for i, j in move:
            cx, cy = x + i, y + j
            if 0 <= cx < 5 and 0 <= cy < 5 and not visited[cx][cy]:
                if place[cx][cy] == 'X':
                    continue
                if place[cx][cy] == 'P':
                    return False
                else:
                    queue.append((cnt + 1, cx, cy))
    return True


def solution(places):
    answer = []
    for place in places:
        isRight = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P': continue
                if not bfs(i, j, place):
                    isRight = 0
                    break
            if not isRight:
                break
        answer.append(isRight)

    return answer


# solution(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"])
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
