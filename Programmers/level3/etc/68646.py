def solution(a):
    n = len(a)
    left = [0] * n
    left[0] = a[0]
    for i in range(1, n):
        left[i] = min(left[i - 1], a[i])

    right = [0] * n
    right[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = min(right[i + 1], a[i])

    answer = 0
    for i in range(n):
        cnt = 0
        if left[i] < a[i]:
            cnt += 1
        if right[i] < a[i]:
            cnt += 1
        if cnt < 2:
            answer += 1
    return answer
solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])