def select(left, right):
    while left < right:
        if string[left] != string[right]:
            return 1
        left += 1
        right -= 1
    return 0


def twopointer(left, right):
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            l = select(left + 1, right)
            r = select(left, right - 1)
            if l == 0 or r == 0:
                return 1
            return 2
    return 0

T = int(input())
for _ in range(T):
    string = input()
    n = len(string)
    print(twopointer(0, n-1))