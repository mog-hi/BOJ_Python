def divide(size, row, col):
    global cnt
    if row == r and col == c:
        print(cnt)
        exit(0)
    if size == 1:
        cnt += 1
        return
    if not (row <= r < row+size and col <= c < col+size):
        cnt += size*size
        return
    divide(size//2, row, col)
    divide(size//2, row, col + size//2)
    divide(size//2, row + size//2, col)
    divide(size//2, row + size//2, col + size//2)
cnt = 0
n, r, c = map(int, input().split())
divide(2**n, 0, 0)