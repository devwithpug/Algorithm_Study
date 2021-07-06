# https://www.acmicpc.net/problem/2468

import sys

def reachable(matrix, visit, x, y, rain):
    return matrix[y][x] > rain and not visit[y][x] 

def find(matrix, visit, x, y, rain):
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):

        _y = y + dy[i]
        _x = x + dx[i]
    
        if 0 <= _y < n and 0 <= _x < n and reachable(matrix, visit, _x, _y, rain):
            visit[_y][_x] = True
            find(matrix, visit, _x, _y, rain)

sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
matrix =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

for rain in range(max(sum(matrix, []))):

    visit = [[False] * n for _ in range(n)]
    num = 0

    for y in range(n):
        for x in range(n):
            if reachable(matrix, visit, x, y, rain):
                visit[y][x] = True
                num += 1
                find(matrix, visit, x, y, rain)
        
    answer = num if num > answer else answer

print(answer)