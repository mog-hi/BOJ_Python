T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    dp = [0]*(x+1)
    dp[0] = 1
    for i in arr:
        for j in range(1, x+1):
            if j >= i:
                dp[j] += dp[j-i]
    print(dp[x])
