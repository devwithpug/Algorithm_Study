# goorm / 기타 / 벡터의 +,- 연산
# https://level.goorm.io/exam/43277/%EB%B2%A1%ED%84%B0%EC%9D%98-%EC%97%B0%EC%82%B0/quiz/1

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
op = input()

print("{}.00 {}.00".format(
    Ax+Bx if op == '+' else Ax-Bx,
    Ay+By if op == '+' else Ay-By
))