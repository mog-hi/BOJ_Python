n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))
dp = [[0, 0, 0] for _ in range(n+1)]
dp[1] = rgb[0]
# 2번
dp[2][0] = min(dp[1][1], dp[1][2]) + rgb[1][0]
dp[2][1] = min(dp[1][0], dp[1][2]) + rgb[1][1]
dp[2][2] = min(dp[1][1], dp[1][0]) + rgb[1][2]
# 3번 ~ n-1번
for i in range(3, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i-1][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + rgb[i-1][2]
# n번
dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + rgb[n-1][0]
dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + rgb[n-1][1]
dp[n][2] = min(dp[n-1][1], dp[n-1][0]) + rgb[n-1][2]
print(min(dp[n]))