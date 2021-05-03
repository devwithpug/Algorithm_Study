# goorm / 기타 / 구름 게임1
# https://level.goorm.io/exam/51584/%EA%B5%AC%EB%A6%84-%EA%B2%8C%EC%9E%841-%EB%AF%B8%EC%99%84%EC%84%B1/quiz/1

n, m = map(int, input().split())
matrix = []

for _ in range(n):
	matrix.append(list(map(int, input().split())))

for _ in range(int(input())):
    line, target = map(int, input().split())
    if line == 0 and target <= n:
        for row in range(m):
            matrix[target-1][row] = 1 if matrix[target-1][row] == 0 else 0
    elif line == 1 and target <= m:
        for col in range(n):
            matrix[col][target-1] = 1 if matrix[col][target-1] == 0 else 0
			
for line in matrix:
    for item in line:
        print(item, end=" ")
    print()