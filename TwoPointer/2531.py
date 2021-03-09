from collections import defaultdict
n, d, k, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))
susi = defaultdict(int)
susi[c] = 1
cnt = 1
for i in range(k):
    if susi[arr[i]] == 0:
        cnt += 1
    susi[arr[i]] += 1
ans = cnt
for left in range(n):
    right = (left+k) % n
    susi[arr[left]] -= 1
    if not susi[arr[left]]:
        cnt -= 1
    if not susi[arr[right]]:
        cnt += 1
    susi[arr[right]] += 1
    ans = max(cnt, ans)
print(ans)
