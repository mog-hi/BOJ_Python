n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
minAns = float('inf')
maxAns = -float('inf')
def dfs(result, loc, add, sub, mul, div):
    global minAns, maxAns
    if loc > n-1:
        minAns = min(minAns, result)
        maxAns = max(maxAns, result)
        return
    if add:
        dfs(result + arr[loc], loc+1, add-1, sub, mul, div)
    if sub:
        dfs(result - arr[loc], loc+1, add, sub-1, mul, div)
    if mul:
        dfs(result * arr[loc], loc+1, add, sub, mul-1, div)
    if div:
        dfs(int(result/arr[loc]), loc+1, add, sub, mul, div-1)
dfs(arr[0], 1, op[0], op[1], op[2], op[3])
print(maxAns)
print(minAns)