# 셔틀버스
from collections import deque
def solution(n, t, m, timetable):
    start = 9*60
    arr = []
    for i in timetable:
        arr.append(int(i[:2])*60+int(i[3:]))
    last = start + (n-1)*t
    arr.sort()
    arr = deque(arr)

    # 마지막 이전 버스에서 내리는 애들
    for i in range(n-1):
        temp = start+i*t
        for j in range(m):
            if arr and arr[0] <= temp:
                arr.popleft()
            else:
                break
    # 마지막 버스도 못타는 애들 제외
    arr = [x for x in arr if x <= last]

    if len(arr) < m:
        answer = last
    else:
        answer = arr[m-1]-1
    answer = str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)
    return answer
solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])
# solution(2, 10, 2, ["09:10", "09:09", "08:00"])
