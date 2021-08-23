import re
n = int(input())
for _ in range(n):
    s = input()
    regex = '(100+1+|01)+'
    if re.fullmatch(regex, s) == None:
        print('NO')
    else:
        print('YES')
