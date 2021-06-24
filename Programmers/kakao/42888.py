# 오픈채팅방
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    nickname = dict()
    for i in record:
        arr = i.split()
        if arr[0] == 'Change' or arr[0] == 'Enter':
            nickname[arr[1]] = arr[2]
    answer = []
    for i in record:
        arr = i.split()
        if arr[0] == 'Enter':
            answer.append(nickname[arr[1]]+'님이 들어왔습니다.')
        elif arr[0] == 'Leave':
            answer.append(nickname[arr[1]]+'님이 나갔습니다.')
    return answer
solution(record)

