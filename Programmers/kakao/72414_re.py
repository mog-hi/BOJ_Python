def play_time_convert(play_time):
    if type(play_time) == str:
        return int(play_time[0:2])*3600 + int(play_time[3:5])*60 + int(play_time[6:])
    return str(play_time//3600).zfill(2)+':'+str((play_time%3600)//60).zfill(2)+':'+str(play_time%60).zfill(2)

def solution(play_time, adv_time, logs):
    answer = 0
    n = play_time_convert(play_time)
    dp = [0]*(n+2)
    for i in logs:
        start, end = play_time_convert(i[:8]), play_time_convert(i[9:])
        dp[start] += 1
        dp[end] -= 1

    for i in range(1, n+1):
        dp[i] += dp[i-1]
    for i in range(1, n+1):
        dp[i] += dp[i-1]

    adv = play_time_convert(adv_time)
    result = dp[adv]
    for start in range(1, n):
        if start + adv >= n:
            end = n
        else:
            end = start+adv
        if result < dp[end]-dp[start]:
            answer = start + 1
            result = dp[end]-dp[start]

    return answer
# solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
# solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
# solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
solution("00:00:08", "00:00:02", ["00:00:02-00:00:06", "00:00:04-00:00:07"])