# n진수 게임
def convert(x, n):
    match = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    answer = ''
    if x == 0: return '0'
    while x > 0:
        a = x//n
        b = x%n
        if b > 9:
            answer = match[b]+answer
        else:
            answer = str(b)+answer
        x = a
    return answer
def solution(n,t,m,p):
    cnt = p+m*(t-1)
    result = ''
    for i in range(cnt):
        y = convert(i, n)
        result += y
    answer = ''
    for i in range(t):
        answer += result[i*m+p-1]
    return answer
solution(2, 4, 2, 1)
print(solution(	16, 16, 2, 2))