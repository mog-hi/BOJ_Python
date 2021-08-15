# 최고의 집합
def solution(n, s):
    if s//n == 0:
        return [-1]
    answer = [s//n]*n
    s %= n
    for i in range(s):
        answer[i % n] += 1
    answer.sort()
    print(answer)
    return answer

# solution(2, 9)
# solution(2, 1)


solution(10000, 100000000)