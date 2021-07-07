import re
def solution(word, pages):
    n = len(pages)
    basic_score = [0]*n
    links = dict()
    # 기본 점수
    for i, item in enumerate(pages):
        arr = re.sub('[^a-z]+', '.', item.lower()).split('.')
        basic_score[i] = arr.count(word.lower())

        finder = '''<meta property="og:url" content="'''
        link_start = item.index(finder)+len(finder)
        link = item[link_start:].split('''"''')[0]
        links[link] = i

    # 외부 링크 수
    out_link = [0]*n
    link_graph = [[0]*n for _ in range(n)]
    for i, item in enumerate(pages):
        out_link[i] = item.count("a href")
        arr = item.split('''a href="''')
        for j in arr:
            to = j.split('''"''')[0]
            if links.get(to) != None:
                link_graph[i][links[to]] = 1

    result = [0]*n
    max_score = 0
    answer = 0
    for i in range(n):
        result[i] = basic_score[i]
        for j in range(n):
            if link_graph[j][i]:
                result[i] += (basic_score[j]/out_link[j])
        if result[i] > max_score:
            answer = i
            max_score = result[i]
    return answer
# solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])