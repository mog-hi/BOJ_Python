n, k = map(int, input().split())
a = list(map(int, input().split()))
box = [0]*(2*n)
t = 1
while True:
    # 1
    temp = [0]*(2*n)
    temp_box = [0]*(2*n)
    for i in range(2*n):
        temp[(i+1)%(2*n)] = a[i]
        temp_box[(i+1)%(2*n)] = box[i]
    a = temp
    box = temp_box

    # 2
    box[n-1] = 0
    for i in range(n-2, -1, -1):
        if box[i]==0: continue
        if a[i+1] > 0 and not box[i+1]:
            a[i+1]-=1
            box[i] = 0
            box[i+1] = 1
    box[n-1] = 0
    # 3
    if not box[0] and a[0] > 0:
        box[0] = 1
        a[0] -= 1

    # 4
    cnt = 0
    for i in range(2*n):
        if a[i] == 0:
            cnt += 1
    if cnt >= k:
        break
    t += 1
print(t)