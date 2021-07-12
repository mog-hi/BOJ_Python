change = dict()
change['zero'] = 0
change['one'] = 1
change['two'] = 2
change['three'] = 3
change['four'] = 4
change['five'] = 5
change['six'] = 6
change['seven'] = 7
change['eight'] = 8
change['nine'] = 9

def solution(s):
    answer = ''
    temp = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if change.get(temp) is not None:
                answer += str(change[temp])
                temp = ''
    return answer

solution("23four5six7")
