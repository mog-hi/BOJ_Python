n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: [x[1], x[0]])
last = 0
answer = 0
for start, end in arr:
    if last <= start:
        answer += 1
        last = end
print(answer)
