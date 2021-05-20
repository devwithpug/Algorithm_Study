# goorm / 기타 / 오염물질 제거하기
# https://level.goorm.io/exam/43081/1e-%EC%98%A4%EC%97%BC%EB%AC%BC%EC%A7%88-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0/quiz/1

def find_formular(x1, y1, x2, y2):
    grad = (y2 - y1) / (x2 - x1)
    y_intercept = -x1 * grad + y1
    return grad, y_intercept
       
t = int(input())
result = []
for _ in range(t):
    n = int(input())
    matrix = []
    answer = 0
    for _ in range(n):
        matrix.append(tuple(map(int, input().split())))

    for x1, y1 in matrix:
        for x2, y2 in matrix:
            tmp = 0
            if x1 == x2:
                for x, y in matrix:
                    if x == x1:
                        tmp += 1
            elif y1 == y2:
                for x, y in matrix:
                    if y == y1:
                        tmp += 1
            else:
                grad, y_i = find_formular(x1, y1, x2, y2)
                for x, y in matrix:
                    if y == x * grad + y_i:
                        tmp += 1
            answer = max(answer, tmp)

    result.append(answer)

for num in result:
    print(num)