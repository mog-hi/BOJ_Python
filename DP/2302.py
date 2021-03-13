n = int(input())
m = int(input())
vip = [False]*(n+1)
for i in range(m):
    vip[int(input())] = True
dp = [1]*(n+1)
for i in range(2, n+1):
    if vip[i] or vip[i-1]:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-2] + dp[i-1]
print(dp[n])