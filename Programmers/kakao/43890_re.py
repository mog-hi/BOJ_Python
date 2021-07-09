from itertools import combinations
def solution(relation):
    candidateKeys = []
    c = len(relation[0])
    for n in range(1, c+1):
        for candidate in list(combinations(range(c), n)):
            # minimality
            minimality = True
            for candidateKey in candidateKeys:
                if len(set(candidate)-set(candidateKey)) == len(candidate) - len(candidateKey):
                    minimality = False
                    break
            if not minimality: continue
            # uniqueness
            uniqueness = True
            arr = []
            for i in range(len(relation)):
                temp = []
                for j in candidate:
                    temp.append(relation[i][j])
                if temp not in arr:
                    arr.append(temp)
                else:
                    uniqueness = False
                    break
                if not uniqueness:
                    break
            if uniqueness:
                candidateKeys.append(candidate)
    return len(candidateKeys)
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])