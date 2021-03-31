def check(left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
def twopointer(left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if check(left+1, right) or check(left, right-1):
                return 1
            return 2
    return 0
T = int(input())
for _ in range(T):
    s = input()
    print(twopointer(0, len(s)-1))