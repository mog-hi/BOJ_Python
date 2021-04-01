import bisect
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[0])
lis = []
for i in range(n):
    lis.append(arr[i][1])
# dp = [1]*n
# for i in range(1, n):
#     for j in range(i):
#         if lis[j] < lis[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(n-max(dp))
dp = []
for i in range(n):
    idx = bisect.bisect_left(dp, lis[i])
    if idx == len(dp):
        dp.append(lis[i])
    else:
        dp[idx] = lis[i]
print(n - len(dp))

