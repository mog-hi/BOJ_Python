n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = arr[n-1]
for i in range(n-1):
    x += arr[i]/2
print(x)