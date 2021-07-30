n, k = map(int, input().split())
arr = list(map(int, input().split()))
diff = []
for i in range(1, n):
    diff.append(arr[i] - arr[i - 1])
diff.sort()

answer = 0
for i in range(n - k):
    answer += diff[i]
print(answer)
