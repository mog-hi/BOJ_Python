T = int(input())
def check(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
def allCheck(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if check(s, left+1, right) or check(s, left, right-1):
                return 1
            else:
                return 2
    return 0
for _ in range(T):
    s = input()
    print(allCheck(s))