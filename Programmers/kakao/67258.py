# 보석 쇼핑
from collections import defaultdict
def solution(gems):
    n = len(set(gems))
    left = 0
    right = 0
    result = []
    temp = defaultdict(int)
    temp[gems[0]] = 1
    cnt = 1
    while left <= right < len(gems):
        if cnt == n:
            result.append([left, right])
            temp[gems[left]] -= 1
            if temp[gems[left]] == 0:
                cnt -= 1
            left += 1
        else:
            right += 1
            if right < len(gems):
                temp[gems[right]] += 1
                if temp[gems[right]] == 1: cnt += 1
            else:
                break
    result.sort(key=lambda x:[x[1]-x[0], x[0]])
    print(result)
    return [result[0][0]+1, result[0][1]+1]

solution(["e"])
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
