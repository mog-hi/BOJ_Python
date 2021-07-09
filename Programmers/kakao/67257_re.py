from itertools import permutations
from copy import deepcopy


def solution(expression):
    answer = 0
    expression = expression.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ')
    expression_arr = expression.split()

    for order in list(permutations(["+", "-", "*"], 3)):
        arr = deepcopy(expression_arr)
        for i in order:
            temp = []
            while arr.count(i) > 0:
                j = 0
                while j < len(arr):
                    if arr[j] == i:
                        x = eval(str(temp.pop()) + i + str(arr[j + 1]))
                        j += 2
                        temp.append(x)
                    else:
                        temp.append(arr[j])
                        j += 1
                arr = temp
        answer = max(answer, abs(arr[0]))
    print(answer)
    return answer


solution("100-200*300-500+20")
solution("50*6-3*2")
