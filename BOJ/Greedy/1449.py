N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
start = arr[0] - 0.5
cnt = 1
for i in range(1, N):
    if start+L < arr[i]+0.5:
        cnt += 1
        start = max(start+L, arr[i]-0.5)
print(cnt)