# goorm / DP / 길 찾기(삼각형)
# https://level.goorm.io/exam/43120/%EA%B8%B8-%EC%B0%BE%EA%B8%B0-%EC%82%BC%EA%B0%81%ED%98%95/quiz/1

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))
        
for y in range(1, n):
    for x in range(len(matrix[y])):
        if x == 0:
            matrix[y][x] += matrix[y-1][x]
        elif x == len(matrix[y]) - 1:
            matrix[y][x] += matrix[y-1][x-1]
        else:
            matrix[y][x] += max(matrix[y-1][x-1], matrix[y-1][x])

print(max(sum(matrix, [])))