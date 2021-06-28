s = input()
n = len(s)
dp = [[0,0] for _ in range(n)]
if s[0] == '0':
    print(0)
    exit(0)
dp[0][0] = 1
dp[0][1] = 0
for i in range(1,n):
    if int(s[i]) > 0:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
    if 10<=int(s[i-1:i+1])<=26:
        dp[i][1] = dp[i-1][0]
print(sum(dp[n-1])%1000000)