n = int(input())
t = [0]*n
earn = [0]*n
dp = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    t[i] = a
    earn[i] = b
    dp[i] = b
for i in range(n - 1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + t[i]] + earn[i])
print(dp[0])
# for i in range(1, n):
#     for j in range(i):
#         if i-j >= t[j]:
#             dp[i] = max(dp[i], dp[j]+earn[i])
# ans = 0
# for i in range(n):
#     if i+t[i] <= n:
#         ans = max(ans, dp[i])
# print(ans)