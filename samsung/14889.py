n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
answer = float('inf')
start, link = [], []
def dfs(loc):
    global answer
    if len(link) == len(start) == n//2:
        a = 0
        b = 0
        for i in range(len(link)):
            for j in range(0, i):
                a += s[link[i]][link[j]] + s[link[j]][link[i]]
        for i in range(len(start)):
            for j in range(0, i):
                b += s[start[i]][start[j]] + s[start[j]][start[i]]
        answer = min(answer, abs(a-b))
        return
    if loc > n-1:
        return
    link.append(loc)
    dfs(loc+1)
    link.pop()
    start.append(loc)
    dfs(loc+1)
    start.pop()
dfs(0)
print(answer)