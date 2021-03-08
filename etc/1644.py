# 소수, 투포인터
n = int(input())
primes = []
# 소수 구하기
check = [True]*(n+1)
for i in range(2, n+1):
    if check[i]:
        primes.append(i)
        for j in range(i+i, n+1, i):
            check[j] = False
s = 0
k = len(primes)
sumarr = [0]*(k+1)
for i in range(len(primes)):
    s += primes[i]
    sumarr[i+1] = s
left = 0
right = 1
answer = 0
while left <= right < k+1:
    x = sumarr[right]-sumarr[left]
    if x < n:
        right += 1
    else:
        if x == n:
            answer += 1
        left += 1
print(answer)