# T가 매우 크니까 T에 대해서 다 하지말고, 하나의 dictionary에 대해서
# adict[item] * bdict[T-item] 로 하는게 메모리에 더 좋다.
from collections import defaultdict
T = int(input())
alen = int(input())
a = list(map(int, input().split()))
blen = int(input())
b = list(map(int, input().split()))

adict = defaultdict(int)
bdict = defaultdict(int)
for i in range(alen):
    s = 0
    for j in range(i, alen):
        s += a[j]
        adict[s] += 1
for i in range(blen):
    s = 0
    for j in range(i, blen):
        s += b[j]
        bdict[s] += 1
answer = 0
for i in adict:
    answer += adict[i]*bdict[T-i]
print(answer)