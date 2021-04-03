# 자물쇠와 열쇠
import copy
def rotation(key, n):
    # key를 그대로 입력받는 것이아니라, key의 돌기 위치 배열을 입력 받고, 회전했을 때 key의 돌기 위치 배열을 반환한다.
    newKey = []
    for i, j in key:
        newKey.append([n-j-1,i])
    return newKey

def solution(key, lock):
    n, m = len(key), len(lock)
    arr = [] # key의 돌기 위치 배열
    for i in range(n):
        for j in range(n):
            if key[i][j]: arr.append([i, j])

    # 비어있는 lock과 lock이 비어있는 부분의 수를 구하기 위한 반복문
    lockBlank = []
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                lockBlank.append([i, j])
    blankCnt = len(lockBlank)

    # 비어있는 lcok이 없다면 무조건 True return
    if blankCnt == 0:
        return True

    # key 돌기가 없다면 False
    if len(arr) == 0: return False

    # 회전 4번에 대해서 검사하기
    for _ in range(4):
        for i in range(len(arr)):
            temp = copy.deepcopy(arr)
            # key의 i번째 돌기가 lock의 홈이 되려면 이동해야 하는 크기 cx와 cy를 구한다.
            cx, cy = lockBlank[0][0]-arr[i][0], lockBlank[0][1] - arr[i][1]

            # 모든 key의 돌기에 cx와 cy를 더해준다.
            for j in range(len(arr)):
                temp[j] = [arr[j][0] + cx, arr[j][1] + cy]

            # key의 돌기가 lock의 홈을 모두 채우는지 + key의 돌기와 lcok의 돌기가 겹치지 않는지 검사
            cnt = 0
            for x, y in temp:
                if 0 <= x < m and 0 <= y < m:
                    if not lock[x][y]:
                        cnt += 1 # key의 돌기 = lock의 홈일 때 cnt++
                    else:
                        break # key의 돌기와 lock의 돌기가 겹침 -> for - else문을 빠져나옴
            else:
                if cnt == blankCnt: # lock의 모든 홈을 채웠을 때
                    return True
        arr = rotation(arr, n)
    return False



# solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])