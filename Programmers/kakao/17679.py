# 프렌즈 4블록
from copy import deepcopy
def solution(m, n, board):
    answer = 0
    while True:
        # erase
        for i in range(m):
            board[i] = list(board[i])
        temp = deepcopy(board)
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    temp[i][j] = '0'
                    temp[i + 1][j] = '0'
                    temp[i][j + 1] = '0'
                    temp[i + 1][j + 1] = '0'
        if temp == board:
            break
        # down
        for i in range(n):
            for j in range(m-1, -1, -1):
                k = j-1
                while temp[j][i] == '0' and k >= 0:
                    temp[j][i],temp[k][i] = temp[k][i],temp[j][i]
                    k -= 1
        board = deepcopy(temp)

    for i in range(m):
        for j in range(n):
            if board[i][j] == '0': answer += 1

    return answer
solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])