import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
result = defaultdict(int)
def dfsLeft(loc, total):
    result[total] += 1
    if loc == half:
        return
    for i in range(loc, half):
        dfsLeft(i + 1, total+arr[i])
    # dfsA(loc + 1, total)
    # dfsA(loc + 1, total + arr[loc])
def dfsRight(loc, total):
    global answer
    answer += result[s-total]
    if loc == n:
        return
    for i in range(loc, n):
        dfsRight(i + 1, total+arr[i])
    # dfsB(loc + 1, total)
    # dfsB(loc + 1, total+arr[loc])
half = n//2
dfsLeft(0, 0)
dfsRight(half, 0)
if s == 0:
    print(answer-1)
else:
    print(answer)
