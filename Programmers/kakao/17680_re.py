from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    print(answer)
    return answer


solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
# solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])