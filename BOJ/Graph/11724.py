# union-find를 쓰지 않을 때
# visited를 만들어 놓고 몇 번의 bfs를 통해 모두 방문할 수 있는지 체크
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rootx] = rooty
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)
cnt = 0
for i in range(1, n+1):
    if parent[i] == i:
        cnt += 1
print(cnt)