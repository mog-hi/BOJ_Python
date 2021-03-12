from collections import deque
import sys
input = sys.stdin.readline
def calc(x, op):
    if op == 'D':
        return (x*2) % 10000
    elif op == 'S':
        if x == 0: return 9999
        return x - 1
    elif op == 'L':
        return (x % 1000)*10 + x//1000
    elif op == 'R':
        a, b, c, d = str(x).zfill(4)
        return (x % 10)*1000 + x//10

def bfs():
    queue = deque()
    queue.append((A, ''))
    visited = [False]*10000
    while queue:
        x, result = queue.popleft()
        if visited[x]: continue
        visited[x] = True
        if x == B:
            print(result)
            break
        queue.append((calc(x, 'D'), result+'D'))
        queue.append((calc(x, 'S'), result+'S'))
        queue.append((calc(x, 'L'), result+'L'))
        queue.append((calc(x, 'R'), result+'R'))
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    bfs()