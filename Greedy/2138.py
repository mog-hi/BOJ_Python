# 이거 꼭 기억해두자.. 잘 안 떠오른다
# 처음이 고정되면 쉽다!!
n = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))
def push(now, idx):
    if idx==0:
        now[idx+1] ^= 1
    elif idx == n-1:
        now[idx-1] ^= 1
    else:
        now[idx-1] ^= 1
        now[idx+1] ^= 1
    now[idx] ^= 1
    return now

def solution(now):
    cnt = 0
    for i in range(1, n):
        if now[i-1] != b[i-1]:
            print(now, "여기오")
            cnt += 1
            now = push(now, i)
    print(now)
    if now == b:
        return cnt
    else:
        return -1

# print(solution(a))
# print(a)
# print(solution(push(a, 0)))
yes = []
yes.extend(push(a, 0))
print(a, yes)