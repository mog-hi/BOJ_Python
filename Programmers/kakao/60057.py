# 문자열 압축
def solution(s):
    res = len(s)
    for cut in range(1, len(s)//2+1):
        answer = ''
        cnt = 1
        last = s[:cut]
        for i in range(cut, len(s), cut):
            if last == s[i: i+cut]:
                cnt += 1
            else:
                if cnt != 1:
                    answer += str(cnt)
                answer += last
                last = s[i: i+cut]
                cnt = 1
        if cnt != 1:
            answer += str(cnt)
        answer += last
        print(answer, len(answer))
        res = min(res, len(answer))
    return res
print(solution('ababcdcdababcdcd'))