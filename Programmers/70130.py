from collections import Counter
def solution(a):
    answer = -1
    cnt = Counter(a)
    n = len(a)
    for k, v in cnt.items():
        if v * 2 < answer: continue
        i = 0
        length = 0
        while i < n - 1:
            if a[i] == a[i+1] or (a[i] != k and a[i+1] != k):
                i += 1
            else:
                i += 2
                length += 2
        answer = max(answer, length)
    print(answer)

    return answer

solution([3, 5,5,7,3,5,5])