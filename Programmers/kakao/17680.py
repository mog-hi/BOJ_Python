from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0: return len(cities) * 5
    for item in cities:
        item = item.lower()
        if item in cache:
            answer += 1
            cache.remove(item)
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
        cache.append(item)
    return answer
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])