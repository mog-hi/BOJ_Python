# 15분
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))
    dp = [[0,0] for _ in range(n+1)]
    dp[1][0] = arr[0][0]
    dp[1][1] = arr[1][0]
    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][1], max(dp[i-2])) + arr[0][i-1]
        dp[i][1] = max(dp[i-1][0], max(dp[i-2])) + arr[1][i-1]
    print(max(dp[n]))