# goorm / 기타 / 피타고라스 문제
# https://level.goorm.io/exam/43279/%ED%94%BC%ED%83%80%EA%B3%A0%EB%9D%BC%EC%8A%A4-%EB%AC%B8%EC%A0%9C/quiz/1

def find():
    for c in range(1, 1000):
        for a in range(1, 1000-c):
            b = 1000 - a - c
            if a**2 + b**2 == c**2:
                print(a*b*c)
                return
            
find()