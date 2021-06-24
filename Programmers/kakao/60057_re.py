# 문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        last = ''
        cnt = 1
        temp = ''
        for j in range(0, len(s), i):
            if last == s[j:j+i]:
                cnt += 1
            else:
                if cnt != 1:
                    temp += str(cnt)
                temp += last
                last = s[j:j+i]
                cnt = 1
        if cnt!=1:
            temp += str(cnt)
        temp += last
        answer = min(answer, len(temp))
    return answer
solution('abcabcdede')