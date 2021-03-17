from collections import deque
n, l = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
def solution(arr):
    up = [False]*n
    for i in range(1, n):
        if arr[i-1] == arr[i]:
            continue
        if abs(arr[i-1]-arr[i]) > 1:
            return False
        if arr[i-1] < arr[i]:
            for j in range(i-1, i-l-1, -1):
                if j < 0 or j > n-1: return False
                if up[j]: return False
                if arr[i-1] != arr[j]: return False
                up[j] = True
        else:
            for j in range(i, i+l):
                if j < 0 or j > n-1: return False
                if up[j]: return False
                if arr[i] != arr[j]: return False
                up[j] = True
    return True
answer = 0
for i in range(n):
    if solution(board[i]): answer += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(board[j][i])
    if solution(temp): answer += 1
print(answer)