import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    parent[x] = y
    # rootx = find(x)
    # rooty = find(y)
    # if rootx != rooty:
    #     parent[rootx] = rooty

g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
arr = []
cnt = 0
for i in range(p):
    arr.append(int(input()))
for i in range(p):
    gate = find(arr[i])
    if gate == 0:
        break
    union(gate, gate-1)
    cnt += 1
print(cnt)