n = int(input())
arr = list(map(int, input().split()))
dp = [[1,1] for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
        elif arr[i] < arr[j]:
            dp[i][0] = max(dp[i][0], max(dp[j]) + 1)
answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))
print(answer)