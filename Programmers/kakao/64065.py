# 튜플
def solution(s):
    answer = []
    s = s[1:-1]
    arr = s.split('},{')
    for i in range(len(arr)):
        arr[i] = arr[i].replace('{', '').replace('}','')
        arr[i] = arr[i].split(',')
    arr.sort(key=lambda x:len(x))
    for j in arr:
        for i in j:
            if int(i) not in answer:
                answer.append(int(i))
    return answer
solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")