import sys
move = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
def spring():
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not tree[i][j]: continue
            new = []
            for x in range(len(tree[i][j])):
                if tree[i][j][x] <= food[i][j]:
                    new.append(tree[i][j][x]+1)
                    food[i][j] -= tree[i][j][x]
                else:
                    temp[i][j] += tree[i][j][x]//2
            tree[i][j] = new

    # summer
    for i in range(N):
        for j in range(N):
            food[i][j] += temp[i][j]
def fall():
    for i in range(N):
        for j in range(N):
            for x in range(len(tree[i][j])):
                if tree[i][j][x]%5 == 0:
                    for k, r in move:
                        cx = i+k
                        cy = j+r
                        if 0<=cx<N and 0<=cy<N:
                            tree[cx][cy].insert(0,1)
def winter():
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]


N, M, K = map(int, input().split())
tree = [[[] for _ in range(N)] for _ in range(N)]
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

food = [[5]*N for _ in range(N)] # 양분
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
for i in range(N):
    for j in range(N):
        tree[i][j].sort()
for _ in range(K):
    spring()
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])
print(answer)

