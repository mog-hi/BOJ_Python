import copy

def move(dir):
    global arr, n
    if dir == 0:
        # left
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if arr[j][i]:
                    temp = arr[j][i]
                    arr[j][i] = 0
                    if arr[j][idx] == 0:
                        arr[j][idx] = temp
                    else:
                        if arr[j][idx] == temp:
                            arr[j][idx] = temp*2
                        else:
                            arr[j][idx+1] = temp
                        idx += 1
    elif dir == 1:
        # right
        for j in range(n):
            idx = n-1
            for i in range(n-2, -1, -1):
                if arr[j][i]:
                    temp = arr[j][i]
                    arr[j][i] = 0
                    if arr[j][idx] == 0:
                        arr[j][idx] = temp
                    else:
                        if arr[j][idx] == temp:
                            arr[j][idx] = temp*2
                        else:
                            arr[j][idx-1] = temp
                        idx -= 1
    if dir == 2:
        # up
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    else:
                        if arr[idx][j] == temp:
                            arr[idx][j] = temp*2
                        else:
                            arr[idx+1][j] = temp
                        idx += 1
    elif dir == 3:
        # down
        for j in range(n):
            idx = n-1
            for i in range(n-2, -1, -1):
                if arr[i][j]:
                    temp = arr[i][j]
                    arr[i][j] = 0
                    if arr[idx][j] == 0:
                        arr[idx][j] = temp
                    else:
                        if arr[idx][j] == temp:
                            arr[idx][j] = temp*2
                        else:
                            arr[idx-1][j] = temp
                        idx -= 1
def dfs(cnt):
    global answer, arr
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                answer = max(answer, arr[i][j])
        return
    temp = copy.deepcopy(arr)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        arr = copy.deepcopy(temp)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
answer = 0
dfs(0)
print(answer)