from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
types = defaultdict(int)
types[c] = 1
answer = 0
cnt = 1
for i in range(k):
    types[arr[i]] += 1
    if types[arr[i]] == 1: cnt += 1
for left in range(1, n):
    right = (left + k - 1) % n
    types[arr[left - 1]] -= 1
    if types[arr[left - 1]] == 0: cnt -= 1
    types[arr[right]] += 1
    if types[arr[right]] == 1: cnt += 1
    answer = max(answer, cnt)
print(answer)
