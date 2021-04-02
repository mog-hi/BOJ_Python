# [1차] 추석 트래픽
def solution(lines):
    answer = 0
    arr = []
    candidate = []
    for i in lines:
        i = i.split()[1:]
        time, T = i
        T = float(T[:-1])
        end = int(time[0:2])*3600 + int(time[3:5])*60 + float(time[6:])
        start = end-T + 0.001
        arr.append((start, end))
        candidate.append(end)
    for i in candidate:
        cnt = 0
        for start, end in arr:
            if not (start>=i+1 or end < i):
                cnt += 1
        answer = max(answer, cnt)
    return answer
# solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
solution([
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
])