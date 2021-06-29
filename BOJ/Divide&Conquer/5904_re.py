n = int(input())
# n 번째를 문자를 구해야 한다. 그건 k번째 시행에 해당한다.
# dp+dfs 문제에 더 까깝다. top->dowm 방식
# k 시행 별로 문자열의 길이를 저장하는 dp
dp = [3]
k = 0
while dp[k] < n:
    k += 1
    dp.append(2*dp[k-1]+k+3)
# dp[k] = k번째 시행했을 때의 길이
# 문자열의 구간 =
# 1. s(k-1)
# 2. m
# 3. o -> k+2
# 4. s(k-1)
# moo(n, k) : k번째 실행에서 n번 문자

def moo(n, k):
    if k == 0:
        return 'moo'[n]
    if n < dp[k-1]: #1
        return moo(n, k-1)
    if n == dp[k-1]: #2
        return 'm'
    if n < dp[k-1]+k+3: #3
        return 'o'
    return moo(n-(k+3)-dp[k-1], k-1) #4
print(moo(n-1, k))