n = int(input())
# dp = [[0,0] for _ in range(n+1)]
# dp[1] = [0, 1]
# for i in range(2, n+1):
#     dp[i][1] = dp[i-1][0]
#     dp[i][0] = sum(dp[i-1])
# print(sum(dp[n]))
dp = [0]*(n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])