# 괄호 변환
# 올바른 문자열인지 판단
def isRight(p):
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        else:
            if not stack: return False
            stack.pop()
    if not stack: return True
    return False
def solution(p):
    if p == '': return ''
    # 2
    left = 0
    right = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
    if isRight(u):
        return u + solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        for i in u[1:-1]:
            if i == '(':
                temp += ')'
            elif i == ')':
                temp += '('
        return temp
print(solution("()))((()"))