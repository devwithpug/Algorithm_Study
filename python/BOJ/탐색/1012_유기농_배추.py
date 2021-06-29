# https://www.acmicpc.net/problem/1012

def find_nearby(matrix, pos, x, y):
    for _x, _y in pos:
        if _x == x and _y == y:
            continue
        if abs(_x - x) <= 1 and abs(_y - y) <= 1 and not (abs(_x - x) == 1 and abs(_y - y)):
            before = matrix[_y][_x]
            matrix[_y][_x] = matrix[y][x]
            for __x, __y in pos:
                if matrix[__y][__x] == before:
                    matrix[__y][__x] = matrix[y][x]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    matrix = [[0 for _ in range(m)] for _ in range(n)]
    pos = []

    for i in range(1, k+1):
        x, y = map(int, input().split())
        matrix[y][x] = i
        pos.append((x, y))
        
    for x, y in pos:
        find_nearby(matrix, pos, x, y)

    end = len(set(sum(matrix, [])))-1
    end = 1 if end == 0 else end
    print(end)
