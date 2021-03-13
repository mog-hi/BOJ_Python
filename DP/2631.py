# lis인거 보자마자 판단! 뿌셨다 lis~
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))