from collections import defaultdict, deque

board = []
for i in range(3):
    board.extend(list(input().split()))
board = ''.join(board)
visited = defaultdict(int)
start = board.index('0')
answer = float('inf')
queue = deque()
queue.append([0, board])
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while queue:
    cnt, temp = queue.popleft()
    idx = temp.find('0')
    if temp == '123456780':
        answer = cnt
        break
    x, y = idx // 3, idx % 3
    for i, j in move:
        cx, cy = i + x, j + y
        child = list(temp)
        if 0 <= cx < 3 and 0 <= cy < 3:
            changeWith = cx * 3 + cy
            child[idx], child[changeWith] = child[changeWith], child[idx]
            child = ''.join(child)
            if not visited[child]:
                visited[child] = 1
                queue.append([cnt + 1, child])
if answer == float('inf'):
    print(-1)
else:
    print(answer)
