n = int(input())
arr = list(map(int, input().split()))
answer = 0

# 누적합 구하기
leftSum = [0] * n
rightSum = [0] * n
leftSum[0] = arr[0]
rightSum[n - 1] = arr[n - 1]
for i in range(1, n):
    leftSum[i] = leftSum[i - 1] + arr[i]
for i in range(n - 2, -1, -1):
    rightSum[i] = rightSum[i + 1] + arr[i]

answer = 0
# 벌통이 왼쪽 끝에 있을 때
temp = 0
one = rightSum[0] - rightSum[n - 1]
for i in range(n - 2, 0, -1):
    two = rightSum[0] - rightSum[i]
    temp = max(temp, two + one - arr[i])
answer = max(answer, temp)

# 벌통이 오른쪽 끝에 있을 때
temp = 0
one = leftSum[n - 1] - leftSum[0]
for i in range(1, n - 1):
    two = leftSum[n - 1] - leftSum[i]
    temp = max(temp, one + two - arr[i])
answer = max(answer, temp)

# 벌통이 중앙에 있을 때
temp = 0
for i in range(1, n - 1):
    temp = max(temp, leftSum[i] - leftSum[0] + rightSum[i] - rightSum[n - 1])

answer = max(answer, temp)
print(answer)
