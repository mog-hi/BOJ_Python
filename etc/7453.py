# 값을 찾는 최고의 방법은 binarysearch 보다도 map(dictionary)이다!!
N = int(input())
A, B, C, D = [], [], [], []
for i in range(N):
    a,b,c,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
AB = dict()
for a in A:
    for b in B:
        AB[a+b] = AB.get(a+b, 0) + 1
answer = 0
for c in C:
    for d in D:
        answer += AB.get(-(c+d), 0)
print(answer)