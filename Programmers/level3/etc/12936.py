def factorial(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer

def solution(n, k):
    answer = []
    k -= 1
    numbers = list(range(1, n+1))
    for i in range(n-1, -1, -1):
        f = factorial(i)
        x = k // f
        answer.append(numbers[x])
        numbers.pop(x)
        k %= f
    return answer


solution(3, 5)