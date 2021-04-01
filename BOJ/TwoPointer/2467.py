n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = n-1
x = 0
y = n-1
result = abs(arr[n-1]+arr[0])
while left < right:
    temp = arr[left]+arr[right]
    if abs(temp) < result:
        result = abs(temp)
        x = left
        y = right
    if temp > 0:
        right -= 1
    else:
        left += 1
print(arr[x], arr[y])