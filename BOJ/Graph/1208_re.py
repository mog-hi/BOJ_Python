from collections import defaultdict

def left_dfs(x, loc):
    left_candidate[x] += 1
    if loc == len(left):
        return
    for i in range(loc, len(left)):
        left_dfs(x + left[i], i + 1)

def right_dfs(x, loc):
    right_candidate[x] += 1
    if loc == len(right):
        return
    for i in range(loc, len(right)):
        right_dfs(x + right[i], i + 1)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
left = arr[:len(arr)//2]
right = arr[len(arr)//2:]

left_candidate = defaultdict(int)
left_dfs(0, 0)
right_candidate = defaultdict(int)
right_dfs(0, 0)

cnt = 0
for num in left_candidate:
    cnt += left_candidate[num]*right_candidate[s-num]
print(cnt - 1 if s == 0 else cnt)