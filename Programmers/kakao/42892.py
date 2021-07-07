import sys
sys.setrecursionlimit(10**6)
graph = []
result = [[], []]


def solution(nodeinfo):
    global graph, result
    n = len(nodeinfo)
    nodeIdx = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        nodeinfo[i - 1].append(i)
        nodeIdx[i] = [nodeinfo[i - 1][0], nodeinfo[i - 1][1]]
    nodeinfo.sort(key=lambda x: [-x[1], x[0]])
    graph = [[0, 0] for _ in range(n + 1)]
    root = nodeinfo[0][2]
    for x, y, node in nodeinfo[1:]:
        par = root
        while par:
            px, py = nodeIdx[par]
            if px > x:
                if graph[par][0] == 0:
                    graph[par][0] = node
                    break
                par = graph[par][0]
            else:
                if graph[par][1] == 0:
                    graph[par][1] = node
                    break
                par = graph[par][1]
    preorder(root)
    postorder(root)
    return result


def preorder(node):
    result[0].append(node)
    if graph[node][0] != 0:
        preorder(graph[node][0])
    if graph[node][1] != 0:
        preorder(graph[node][1])


def postorder(node):
    if graph[node][0] != 0:
        postorder(graph[node][0])
    if graph[node][1] != 0:
        postorder(graph[node][1])
    result[1].append(node)


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
# solution([])
