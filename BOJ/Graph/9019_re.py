from collections import deque
T = int(input())
def calc(x, op):
    if op == 'D':
        return (x*2)%10000
    elif op =='S':
        if x == 0: return 9999
        return x-1
    elif op == 'L':
        return (x%1000)*10+x//1000
    else:
        return (x%10)*1000+x//10

for _ in range(T):
    a, b = map(int, input().split())
    queue = deque()
    queue.append([a, ''])
    visited = [False]*10000
    while queue:
        x, op = queue.popleft()
        if visited[x]: continue
        visited[x] = 1
        if x == b:
            print(op)
            break
        queue.append([calc(x, 'D'), op+'D'])
        queue.append([calc(x, 'S'), op+'S'])
        queue.append([calc(x, 'L'), op+'L'])
        queue.append([calc(x, 'R'), op+'R'])
