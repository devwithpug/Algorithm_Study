# goorm / 탐색 / 다익스트라 알고리즘
# https://level.goorm.io/exam/43211/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-dijkstra-s-algorithm/quiz/1

import sys

def search(dic, st, cnt, e, cost, result_cost):
    if cnt == e:
        return
    for path in dic[st]:
        if result_cost[path[0]-1] > cost+path[1]:
            result_cost[path[0]-1] = cost+path[1]
        search(dic, path[0], cnt+1, e, cost+path[1], result_cost)

n, e = map(int, input().split())
dic = {}

for _ in range(e):
    st, ed, cost = map(int, input().split())
    dic.setdefault(st, [])
    dic.setdefault(ed, [])
    dic[st].append([ed, cost])
    dic[ed].append([st, cost])
start = int(input())

result_cost = [sys.maxsize for _ in range(n)]
result_cost[start-1] = 0
search(dic, start, 0, e, 0, result_cost)

for i in range(n):
    print("{}: {}".format(i+1, result_cost[i]))