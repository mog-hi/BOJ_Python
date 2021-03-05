n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    answer = sum(arr) - max(arr)
else:
    a = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
    a.sort()
    one = a[0]
    two = a[0] + a[1]
    three = a[0] + a[1] + a[2]
    answer = one *((n-2)**2 + (n-2)*(n-1)*4) + two * ((n-2)*4+(n-1)*4) + three*4
print(answer)
