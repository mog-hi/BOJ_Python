def solution(routes):
    answer = 0
    n = len(routes)
    routes.sort(key=lambda x:x[1])
    camera = -float('inf')
    for i in range(n):
        start, end = routes[i]
        if start > camera:
            answer += 1
            camera = end
    return answer

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])