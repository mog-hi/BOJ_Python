from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for node in graph:
        graph[node].sort(reverse=True)
    stack = ['ICN']
    answer = []
    while stack:
        temp = stack[-1]
        if not graph[temp]:
            answer.append(stack.pop())
            continue
        stack.append(graph[temp].pop())
    answer.reverse()
    return answer
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])