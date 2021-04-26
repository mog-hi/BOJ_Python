import sys
input = sys.stdin.readline
n = int(input())
t = [0]*n
p = [0]*n
for i in range(n):
    t[i], p[i] = map(int, input().split())
dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    if i+t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+t[i]] + p[i], dp[i+1])
print(dp[0])