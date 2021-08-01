n = int(input())
s = input()
blue = 0
red = 0
# 연속 개수
b = 0
r = 0
for i in s:
    if i == 'B':
        b += 1
        if r > 0:
            red += 1
            r = 0
    else:
        r += 1
        if b > 0:
            blue += 1
            b = 0
if b > 0 : blue += 1
if r > 0 : red += 1
print(1+min(blue, red))