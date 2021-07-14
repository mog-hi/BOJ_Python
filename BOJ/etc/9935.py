def solution(s, t):
    stack = []
    lastStr = t[-1]
    n = len(t)
    answer = 0
    for i in range(len(s)):
        stack.append(s[i])
        if s[i] == lastStr:
            if len(stack) >= n and ''.join(stack[len(stack) - n:]) == t:
                for j in range(n):
                    stack.pop()
                answer += 1
    # return answer
    if not stack:
        print('FRULA')
    else:
        print(''.join(stack))

s = input()
t = input()
solution(s, t)
