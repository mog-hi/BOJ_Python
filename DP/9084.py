T = int(input())
for _ in range(T):
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1
    for i in money:
        for j in range(1, m+1):
            if j -i >= 0:
                dp[j] += dp[j-i]
    print(dp[m])