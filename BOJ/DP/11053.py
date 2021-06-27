# LIS
# 그냥 DP로 구하기
N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# Binary search
import bisect
N = int(input())
arr = list(map(int, input().split()))
dp = []
for i in range(N):
    idx = bisect.bisect_left(dp, arr[i])
    if idx == len(dp):
        dp.append(arr[i])
    else:
        dp[idx] = arr[i]
print(len(dp))