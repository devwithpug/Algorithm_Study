# goorm / 기타 / 유클리드 호제법
# https://level.goorm.io/exam/43091/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95/quiz/1



a, b = map(int, input().split())

while a % b != 0:
    a, b = b, a % b
    
print(b)