# N으로 표현
from collections import deque, defaultdict
def solution(n, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(n)*i))
    if number in dp[1]:
        return 1
    for x in range(2, 9):
        for i in range(x):
            for a in dp[i]:
                for b in dp[x-i]:
                    dp[x].add(a+b)
                    dp[x].add(a-b)
                    dp[x].add(a*b)
                    if b != 0:
                        dp[x].add(a//b)
        if number in dp[x]:
            return x
    return -1
solution(5, 12)