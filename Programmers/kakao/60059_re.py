def rotate(key):
    n = len(key)
    newKey = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newKey[n - j - 1][i] = key[i][j]
    return newKey


def check(x, y, key, lock):
    n = len(lock)
    m = len(key)
    for i in range(n):
        for j in range(n):
            cx, cy = i - x, j - y
            if not (0 <= cx < m and 0 <= cy < m):
                if lock[i][j] == 0:
                    return False
                continue
            if lock[i][j] == 0 and key[cx][cy] != 1:
                return False
            if lock[i][j] == 1 and key[cx][cy] == 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    isNotLock = True
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                isNotLock = False
                break
    if isNotLock:
        return True

    for i in range(4):
        key = rotate(key)
        keyArr = []
        for i in range(m):
            for j in range(m):
                if key[i][j]: keyArr.append([i, j])

        for i in range(n):
            for j in range(n):
                if lock[i][j] == 1: continue
                for r, c in keyArr:
                    x, y = i - r, j - c
                    if check(x, y, key, lock):
                        return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
