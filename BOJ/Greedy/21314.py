s = input()

maxAnswer = ''
cnt = 0
for i in range(0, len(s)):
    if s[i] == 'K':
        maxAnswer += '5'+'0'*cnt
        cnt = 0
    else:
        cnt += 1
if cnt != 0:
    maxAnswer += '1'*cnt
print(int(maxAnswer))

minAnswer = ''
cnt = 0
for i in range(0, len(s)):
    if s[i] == 'K':
        if cnt > 0:
            minAnswer += '1'+'0'*(cnt-1)
        minAnswer += '5'
        cnt = 0
    else:
        cnt += 1
if cnt > 0:
    minAnswer += '1' + '0' * (cnt - 1)
print(int(minAnswer))