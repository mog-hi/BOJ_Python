# 수식최대화
from itertools import permutations
def solution(expression):
    op = []
    if '+' in expression: op.append('+')
    if '-' in expression: op.append('-')
    if '*' in expression: op.append('*')
    candi = list(permutations(op, len(op)))
    expression = expression.replace('*', ' * ').replace('+',' + ').replace('-',' - ')
    answer = 0
    for ops in candi:
        arr = expression.split()
        print(ops)
        for i in ops:
            temp = []
            j = 0
            while j < len(arr):
                if arr[j] == i:
                    x = temp[-1]+i+arr[j+1]
                    temp = temp[:-1]
                    temp.append(str(eval(x)))
                    j += 2
                else:
                    temp.append(arr[j])
                    j+=1
            arr = temp
        answer = max(answer, abs(int(temp[0])))
    return answer

print(solution("100-200*300-500+20"))