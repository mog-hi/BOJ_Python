def solution(s):
    answer = 0
    n = len(s)

    def check(start, end):
        while 0 <= start < end < n:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    for start in range(n):
        for end in range(n-1, start, -1):
            if check(start, end):
                answer = max(answer, end-start+1)
                break

    print(answer)
    return answer
solution("ab")