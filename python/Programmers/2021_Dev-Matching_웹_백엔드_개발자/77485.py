# https://programmers.co.kr/learn/courses/30/lessons/77485

def do_circle(matrix, size, x1, y1, x2, y2):
    min_num = size
    tmp = 0

    for i in range(x1, x2):
        tmp, matrix[y1][i] = matrix[y1][i], tmp
        min_num = min(min_num, tmp)

    for i in range(y1, y2):
        tmp, matrix[i][x2] = matrix[i][x2], tmp
        min_num = min(min_num, tmp)

    for i in range(x2, x1, -1):
        tmp, matrix[y2][i] = matrix[y2][i], tmp
        min_num = min(min_num, tmp)

    for i in range(y2, y1, -1):
        tmp, matrix[i][x1] = matrix[i][x1], tmp
        min_num = min(min_num, tmp)

    matrix[y1][x1] = tmp
    return min_num
    

def solution(rows, columns, queries):
    answer = []

    matrix = [[j + i * columns for j in range(1, columns+1)] for i in range(rows)]

    for y1, x1, y2, x2 in queries:
        min_num = do_circle(matrix, rows * columns, x1-1, y1-1, x2-1, y2-1)
        answer.append(min_num)

    return answer


rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
