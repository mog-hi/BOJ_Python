n = int(input())
arr = []
allCnt = 0
for i in range(n):
    x, a = map(int, input().split())
    arr.append([x, a])
arr.sort()
sumArr = [0] * n
sumArr[0] = arr[0][1]
for i in range(1, n):
    sumArr[i] = sumArr[i - 1] + arr[i][1]

l = 0
r = n - 1
pos = float('inf')
while l <= r:
    mid = (l + r) // 2
    leftSum = sumArr[mid]
    rightSum = sumArr[n - 1] - sumArr[mid]
    if leftSum >= rightSum:
        r = mid - 1
        pos = min(pos, arr[mid][0])
    else:
        l = mid + 1
print(pos)
