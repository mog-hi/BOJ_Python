# 기둥과 보 설치
def bo_check(x, y, bo, piller):
    n = len(bo)
    if (y>0 and piller[x][y-1]) or (y>0 and x<n and piller[x+1][y-1]) or (bo[x-1][y] and bo[x+1][y]):
        return True
    return False

def piller_check(x, y, bo, piller):
    if bo[x][y] or (x > 0 and bo[x - 1][y]) or y == 0 or piller[x][y - 1]:
        return True
    return False

def delete_check(bo, piller):
    n = len(bo)
    for x in range(n):
        for y in range(n):
            if bo[x][y] and not bo_check(x, y, bo, piller):
                return False
            if piller[x][y] and not piller_check(x, y, bo, piller):
                return False
    return True

def solution(n, build_frame):
    piller = [[0]*(n+1) for _ in range(n+1)]
    bo = [[0]*(n+1) for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 1: # 추가
            if a == 1: # 보
                if bo_check(x, y, bo, piller):
                    bo[x][y] = 1
            elif a == 0:
                if piller_check(x, y, bo, piller):
                    piller[x][y] = 1
        else:
            if a == 1:
                bo[x][y] = 0
                if not delete_check(bo, piller):
                    bo[x][y] = 1
            elif a == 0:
                piller[x][y] = 0
                if not delete_check(bo, piller):
                    piller[x][y] = 1

    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if piller[i][j]:
                answer.append([i, j, 0])
            if bo[i][j]:
                answer.append([i, j, 1])
    print(answer)
    return answer

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])