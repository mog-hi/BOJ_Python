def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    visited = set()
    visited.add(costs[0][0])
    visited.add(costs[0][1])
    answer = costs[0][2]
    costs.pop(0)
    while len(visited) != n:
        for idx, item in enumerate(costs):
            i, j, cost = item
            if len(visited) == n: break
            if i in visited and j in visited:
                continue
            if i in visited or j in visited:
                visited.add(i)
                visited.add(j)
                answer += cost
                costs.pop(idx)
                break
    return answer
solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])