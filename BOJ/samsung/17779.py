def calculate(x, y, d1, d2):
    arr = [0,0,0,0,0]
    temp = [[0]*n for _ in range(n)]
    for i in range(d1+1):
        temp[x+i][y-i] = 5
        temp[x+d2+i][y+d2-i]=5
    for j in range(d2+1):
        temp[x+j][y+j] = 5
        temp[x+d1+j][y-d1+j] = 5

    for i in range(x+d1):
        c = 0
        while temp[i][c] == 0 and c<=y:
            arr[0] += a[i][c]
            c+=1
    for i in range(x + d2+1):
        c = n-1
        while temp[i][c] == 0 and c>y:
            arr[1] += a[i][c]
            c-=1
    for i in range(x+d1, n):
        c = 0
        while temp[i][c] == 0 and c < y-d1+d2:
            arr[2] += a[i][c]
            c+=1
    for i in range(x + d2 +1, n):
        c = n-1
        while temp[i][c] == 0 and c>=y-d1+d2:
            arr[3] += a[i][c]
            c-=1
    arr[4] = total-sum(arr)
    return abs(max(arr)-min(arr))

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

answer = float('inf')
total = 0
for i in range(n):
    total += sum(a[i])

for x in range(0, n):
    for y in range(0, n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x+d1+d2 < n and y-d1>=0 and y+d2<n:
                    answer = min(answer, calculate(x, y, d1, d2))
print(answer)