# goorm / 기타 / 놀이공원
# https://level.goorm.io/exam/88520/%EB%86%80%EC%9D%B4%EA%B3%B5%EC%9B%90/quiz/1

t = int(input())
answer = []

for _ in range(t):
    n, k = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
        
    result = []

    for y in range(n-k+1):
        for x in range(n-k+1):
            result.append(sum(sum([row[x:x+k] for row in matrix[y:y+k]], [])))

    answer.append(min(result))
    
for a in answer:
    print(a)