from collections import defaultdict


def solution(genres, plays):
    answer = []
    n = len(genres)
    genresCnt = defaultdict(int)
    playsByGenres = defaultdict(list)
    for i in range(n):
        genresCnt[genres[i]] += plays[i]
        playsByGenres[genres[i]].append(i)
    genresCnt = list(genresCnt.items())
    genresCnt.sort(key=lambda x: -x[1])
    for key in playsByGenres:
        playsByGenres[key].sort(key=lambda x: [-plays[x], x])
    for genre, cnt in genresCnt:
        answer.extend(playsByGenres[genre][:2])

    return answer


solution(["classic", "pop", "classic", "classic"], [500, 600, 150, 800])
