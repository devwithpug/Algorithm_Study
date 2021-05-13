# goorm / 기타 / 어느 개발자 이야기
# https://level.goorm.io/exam/43171/%EC%96%B4%EB%8A%90-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B4%EC%95%BC%EA%B8%B0/quiz/1

from math import sqrt

k = input()
num = int(max(list(k)))

for i in range(num+1, 100):
    t = int(k, i)
    if int(sqrt(t)) == sqrt(t):
        print(i)
        break