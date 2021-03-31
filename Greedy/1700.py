n, k = map(int, input().split())
arr = list(map(int, input().split()))
plugin = []
answer = 0
for i in range(k):
    if arr[i] in plugin:
        continue
    if len(plugin) < n:
        plugin.append(arr[i])
        continue
    out = 0
    outidx = 0
    answer += 1
    for j in range(n):
        try:
            idx = arr[i+1:].index(plugin[j])
            if idx > outidx:
                out = j
                outidx = idx
        except:
            out = j
            break
    plugin[out] = arr[i]
print(answer)


