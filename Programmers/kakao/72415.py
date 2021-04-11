from collections import deque
from itertools import permutations
from copy import deepcopy

board = []
def ctrl_move(r, c, k, t):
    global board
    cr, cc = r, c
    while True:
        nr = cr + k
        nc = cc + t
        if not (0<=nr<4 and 0<=nc<4):
            return cr, cc
        if board[nr][nc] != 0:
            return nr, nc
        cr = nr
        cc = nc
def bfs(start, end):
    r, c = start
    find_r, find_c = end
    queue = deque()
    queue.append((r, c, 0))
    visited = [[0]*4 for _ in range(4)]
    move = [(0,-1),(0,1),(-1,0),(1,0)]
    while queue:
        r, c, temp = queue.popleft()
        if visited[r][c]: continue
        visited[r][c] = 1
        if r == find_r and c == find_c:
            return temp
        for k, t in move:
            cr = k+r
            cc = c+t
            if 0<=cr<4 and 0<=cc<4:
                queue.append((cr,cc, temp+1))
            cr, cc = ctrl_move(r, c, k, t)
            queue.append((cr, cc, temp+1))
    return -1

def solution(input_board, sr, sc):
    global board
    board = input_board
    location = [[] for _ in range(7)]
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in nums: nums.append(board[i][j])
                location[board[i][j]].append((i, j))
    per = list(permutations(nums, len(nums)))
    answer = float('inf')
    for i in range(len(per)):
        board = deepcopy(input_board)
        cnt = 0
        r, c = sr, sc
        for j in per[i]:
            left = bfs((r, c), location[j][0])
            right = bfs((r, c), location[j][1])
            if left < right:
                cnt += left
                cnt += bfs(location[j][0], location[j][1])
                r, c = location[j][1]
            else:
                cnt += right
                cnt += bfs(location[j][1], location[j][0])
                r, c = location[j][0]
            board[location[j][0][0]][location[j][0][1]] = 0
            board[location[j][1][0]][location[j][1][1]] = 0
            cnt += 2 # enter
        answer = min(answer, cnt)
    return answer
solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)
# solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1)