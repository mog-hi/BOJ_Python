def control(m):
    m = m.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
    return m

def solution(m, musicinfos):
    result = []
    for i in musicinfos:
        start, end, name, music = i.split(',')
        time = abs((int(start[:2])*60 + int(start[3:])) - (int(end[:2])*60 + int(end[3:])))
        play = ''
        music = control(music)
        for j in range(time):
            play += music[j%len(music)]
        m = control(m)
        if m in play:
            result.append([name, time])
    if not result:
        return '(None)'
    result.sort(key=lambda x:-x[1])
    return result[0][0]
solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
# solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])