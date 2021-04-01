T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxarr = [0]*N
    maxarr[N-1] = arr[N-1]
    for i in range(N-2, -1, -1):
        maxarr[i] = max(maxarr[i+1], arr[i])
    answer = 0
    for i in range(N):
        answer += maxarr[i]-arr[i]
    print(answer)