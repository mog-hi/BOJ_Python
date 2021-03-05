arr = list(map(int, list(input())))
n = len(arr)
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
if arr[0] == 0:
    print(0)
else:
    for i in range(2, n+1):
        if arr[i-1] > 0:
            dp[i] += dp[i-1]
        if 10 <= arr[i-2]*10 + arr[i-1] <= 26:
            dp[i] += dp[i-2]
    print(dp[n]%1000000)