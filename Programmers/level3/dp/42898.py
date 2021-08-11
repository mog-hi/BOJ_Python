def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    puddleCheck = [[0] * m for _ in range(n)]
    for i, j in puddles:
        puddleCheck[j-1][i-1] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            if puddleCheck[i][j]: continue
            if i - 1 >= 0 and not puddleCheck[i - 1][j]:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0 and not puddleCheck[i][j - 1]:
                dp[i][j] += dp[i][j - 1]
    return dp[n-1][m-1]


solution(4, 3, [[2, 2]])
