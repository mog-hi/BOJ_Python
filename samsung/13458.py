import math
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
answer = n
for i in arr:
    r = max(i-b, 0)
    answer += math.ceil(r/c)
print(answer)