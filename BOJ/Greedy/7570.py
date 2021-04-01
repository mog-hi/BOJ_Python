n = int(input())
arr = list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(n):
    dp[arr[i]] = dp[arr[i]-1] + 1
print(n-max(dp))