from collections import defaultdict
def solution(msg):
    answer = []
    dictionary = defaultdict(int)
    for i in range(1, 27):
        dictionary[chr(i+64)] = i
    idx = 27
    j = 0
    while j < len(msg):
        for i in range(j, len(msg)):
            if not dictionary[msg[j:i+1]]:
                dictionary[msg[j:i+1]] = idx
                idx+=1
                answer.append(dictionary[msg[j:i]])
                j = i
                break
        else:
            if j < len(msg):
                answer.append(dictionary[msg[j:]])
            break
    return answer
solution('KAKAO')