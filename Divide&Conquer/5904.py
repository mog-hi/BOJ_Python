import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
idx = 0
dp = [3]
k = 0
while dp[k] < n:
    k += 1
    dp.append(2*dp[k-1]+k+3)
def moo(n, k):
    if k == 0:
        return 'moo'[n-1]
    if n <= dp[k-1]:
        return moo(n, k-1)
    if n == dp[k-1] + 1:
        return 'm'
    if n <= dp[k-1] + k + 3:
        return 'o'
    return moo(n-dp[k-1]-k-3, k-1)
print(moo(n, k))