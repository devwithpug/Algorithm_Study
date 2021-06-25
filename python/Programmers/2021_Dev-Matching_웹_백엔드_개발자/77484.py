# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    
    answer = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}

    worst = 0

    for n in lottos:
        if n in win_nums:
            worst += 1
    best = worst + lottos.count(0)

    return [answer[best], answer[worst]]