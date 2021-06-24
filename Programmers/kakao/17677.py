# 뉴스 클러스터링
from collections import defaultdict
import math

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    a = defaultdict(int)
    b = defaultdict(int)
    for i in range(1, len(str1)):
        if str1[i-1:i+1].isalpha():
            a[str1[i-1:i+1]] += 1
    for i in range(1, len(str2)):
        if str2[i-1:i+1].isalpha():
            b[str2[i-1:i+1]] += 1
    uni = 0
    inter = 0
    for i in a:
        if b[i] > 0:
            inter += min(b[i], a[i])
            uni += max(b[i], a[i])
        else:
            uni += a[i]
    for i in b:
        if a[i] == 0:
            uni += b[i]
    if uni == 0:
        return 65536
    return math.floor((inter/uni)*65536)




print(solution('aa1+aa2', 'AAAA12'))