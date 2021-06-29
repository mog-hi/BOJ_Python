N, r, c = map(int, input().split())
t = 0
def dfs(n, x, y):
    global t
    if x == r and y == c:
        print(t)
        exit(0)
    if n == 1:
        t += 1
        return
    if not (0<=r<x+n and 0<=c<y+n):
        t += n**2
        return
    dfs(n//2, x, y)
    dfs(n//2, x, y+n//2)
    dfs(n//2, x+n//2, y)
    dfs(n//2, x+n//2, y+n//2)
dfs(2**N, 0, 0)
