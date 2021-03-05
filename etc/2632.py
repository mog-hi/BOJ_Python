from collections import defaultdict
k = int(input())
m, n = map(int, input().split())
A = []
B = []
for i in range(m):
    A.append(int(input()))
for i in range(n):
    B.append(int(input()))
adict = defaultdict(int)
adict[sum(A)] = 1
for i in range(m):
    j = i
    s = 0
    for _ in range(m-1):
        s += A[j]
        adict[s] += 1
        j = (j+1)%m
bdict = defaultdict(int)
bdict[sum(B)] = 1
for i in range(n):
    j = i
    s = 0
    for _ in range(n-1):
        s += B[j]
        bdict[s] += 1
        j = (j+1)%n
answer = adict[k] + bdict[k]
for i in range(1, k):
    answer += adict[i]*bdict[k-i]
print(answer)