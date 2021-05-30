# goorm / 기타 / 재고없는 날
# https://level.goorm.io/exam/100817/15회-e-pper-3번/quiz/1

n, m = map(int, input().split())

answer = 0
i = 0
while n > 0:
    i += 1
    if i == m:
        n += 1
        i = 0
    n -= 1
    answer += 1

print(answer)
