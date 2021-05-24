# goorm / 기타 / 스테인 알고리즘
# https://level.goorm.io/exam/43200/%EC%8A%A4%ED%85%8C%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/quiz/1

a, b = map(int, input().split())
cnt = 0
while a > 0 and b > 0:
    if a % 2 != 0 and b % 2 != 0:
        if a > b:
            a -= b
        else:
            b -= a
    elif a % 2 == 0 and b % 2 == 0:
        a = int(a / 2)
        b = int(b / 2)
        cnt += 1 
    else:
        a = int(a / 2) if a % 2 == 0 else a
        b = int(b / 2) if b % 2 == 0 else b

print(2**cnt * max(a, b))
    