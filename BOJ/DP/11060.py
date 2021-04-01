n = int(input())
arr = list(map(int, input().split()))
dp = [float('inf')]*n
dp[0] = 0
for i in range(n):
    for j in range(i, min(i + arr[i]+1, n)):
        dp[j] = min(dp[j], dp[i]+1)
if dp[n-1] == float('inf'):
    print(-1)
else:
    print(dp[n-1])