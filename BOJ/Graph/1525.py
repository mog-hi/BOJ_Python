from collections import deque
arr = []
for i in range(3):
    arr.extend(input().split())
depth = dict()
start = ''.join(arr)
queue = deque()
queue.append(start)
depth[start] = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while queue:
    temp = queue.popleft()
    if temp == '123456780':
        break
    idx = temp.find('0')
    x = idx // 3
    y = idx % 3
    for i, j in move:
        cx = x + i
        cy = y + j
        if 0 <= cx < 3 and 0 <= cy < 3:
            arr = list(temp)
            arr[idx], arr[cx*3+cy] = arr[cx*3+cy], arr[idx]
            if not depth.get(''.join(arr), False):
                depth[''.join(arr)] = depth[temp] + 1
                queue.append(''.join(arr))
            arr[idx], arr[cx*3+cy] = arr[cx*3+cy], arr[idx]
if depth.get('123456780', -1) == -1:
    print(-1)
else:
    print(depth['123456780'])