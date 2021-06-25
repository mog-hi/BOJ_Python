from itertools import combinations
from collections import defaultdict
def solution(relation):
    n = len(relation[0])
    result = []
    for cnt in range(1, n + 1):
        arr = list(combinations(range(n), cnt))
        # 유일성 검사
        for candi in arr:
            test = defaultdict(int) # 이걸 한 scope 밖에 써서 틀렸다. 이딴걸 틀리고 찾지도 못하다니
            for re in relation:
                key = ''
                for i in candi:
                    key += re[i]
                if test[key] != 0:
                    break
                test[key] = 1
            else:
                # 최소성 검사
                for already in result:
                    if not set(already) - set(candi):
                        break
                else:
                    result.append(candi)
    return len(result)
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])