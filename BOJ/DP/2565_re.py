n = int(input())
arr = [0]*501
for _ in range(n):
    a, b = map(int, input().split())
    arr[a] = b
dp = [1]*501
for i in range(501):
    if arr[i] == 0: continue
    for j in range(i):
        if arr[j]!=0 and arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))