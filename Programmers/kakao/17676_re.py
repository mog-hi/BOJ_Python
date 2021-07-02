# 추석 트래픽
from decimal import Decimal
def solution(lines):
    arr = []
    for i in lines:
        date, end, s = i.split()
        end = float(end[6:])+int(end[0:2])*3600+int(end[3:5])*60
        start = float(Decimal(str(end))-Decimal(s[:-1])+ Decimal(0.001))
        arr.append([start, end])
    arr.sort(key=lambda x:x[1])
    answer = 0
    for i in range(len(arr)):
        s, e = arr[i]
        cnt = 0
        for j in range(i, len(arr)):
            if arr[j][0] < e+1:
                cnt += 1
        answer = max(answer, cnt)

    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
solution(lines)