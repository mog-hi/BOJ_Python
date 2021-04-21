gear = []
for i in range(4):
    gear.append(list(map(int, list(input()))))
k = int(input())
def turn(num, dir):
    new = [0]*8
    for i in range(8):
        if dir == -1:
            new[i] = gear[num][(i+1)%8]
        else:
            new[i] = gear[num][(i+7)%8]
    gear[num] = new

for i in range(k):
    num, dir = map(int, input().split())
    num -= 1
    arr = []
    d = -dir
    for j in range(num-1, -1, -1):
        if gear[j][2] != gear[j+1][6]:
            arr.append((j, d))
            d *= -1
        else:
            break
    d = -dir
    for j in range(num+1, 4):
        if gear[j-1][2] != gear[j][6]:
            arr.append((j, d))
            d *= -1
        else:
            break
    for n, d in arr:
        turn(n, d)
    turn(num, dir)
answer = 0
if gear[0][0] == 1: answer+=1
if gear[1][0] == 1: answer+=2
if gear[2][0] == 1: answer+=4
if gear[3][0] == 1: answer+=8
print(answer)
