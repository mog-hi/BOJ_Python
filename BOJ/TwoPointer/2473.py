n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = [0, 0, 0, float('inf')]
for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]
        if abs(temp) < abs(answer[3]):
            answer = [i, left, right, temp]
        if temp > 0:
            right -= 1
        elif temp < 0:
            left += 1
        else:
            print(arr[i], arr[left], arr[right])
            exit()
for i in answer[:3]:
    print(arr[i], end=" ")