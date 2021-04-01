import sys
input = sys.stdin.readline
while True:
    try:
        x = int(input())
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(int(input()))
        x *= 10000000
        arr.sort()
        left = 0
        right = n-1
        isAble = False
        while left < right:
            temp = arr[left] + arr[right]
            if temp < x:
                left += 1
            elif temp == x:
                isAble = True
                break
            else:
                right -= 1
        if isAble:
            print('yes', arr[left], arr[right])
        else:
            print('danger')
    except:
        break