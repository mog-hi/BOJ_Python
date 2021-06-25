# 파일명 정렬
def solution(files):
    answer = []
    arr = []
    for i in files:
        head = ''
        number = ''
        for j in i:
            if j.isdigit():
                number += j
            else:
                if number == '':
                    head += j
                else:
                    break
        arr.append([i, head.lower(), int(number)])

    arr.sort(key=lambda x:[x[1], x[2]])
    for i in arr:
        answer.append(i[0])
    return answer
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])