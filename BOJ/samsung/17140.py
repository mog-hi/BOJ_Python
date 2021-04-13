from collections import defaultdict
R, C, K = map(int, input().split())
a = []
for i in range(3):
    a.append(list(map(int, input().split())))
answer = 0
for t in range(100):
    r = len(a)
    c = len(a[0])
    if r >= R and c >= C and a[R-1][C-1] == K:
        break
    answer += 1
    if r >= c:
        maxC = 0
        arr = [[] for _ in range(r)]
        for i in range(r):
            cnt = defaultdict(int)
            for j in range(c):
                if a[i][j] == 0: continue
                cnt[a[i][j]] += 1
            arr[i] = list(cnt.items())
            arr[i].sort(key=lambda x: [x[1], x[0]])
            maxC = max(maxC, len(arr[i])*2)
        temp = [[0]*maxC for _ in range(r)]
        for i in range(r):
            k = 0
            for j in range(len(arr[i])):
                temp[i][k] = arr[i][j][0]
                temp[i][k+1] = arr[i][j][1]
                k += 2
    else:
        maxR = 0
        arr = [[] for _ in range(c)]
        for i in range(c):
            cnt = defaultdict(int)
            for j in range(r):
                if a[j][i] == 0: continue
                cnt[a[j][i]] += 1
            arr[i] = list(cnt.items())
            arr[i].sort(key=lambda x: [x[1], x[0]])
            maxR = max(maxR, len(arr[i])*2)
        temp = [[0]*c for _ in range(maxR)]
        for i in range(c):
            k = 0
            for j in range(len(arr[i])):
                temp[k][i] = arr[i][j][0]
                temp[k+1][i] = arr[i][j][1]
                k += 2
    a = temp
if r >= R and c >= C and a[R-1][C-1] == K:
    print(answer)
else:
    print(-1)