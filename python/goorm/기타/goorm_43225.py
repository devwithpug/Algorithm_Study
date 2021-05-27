# goorm / 기타 / 돈이 급한 남자
# https://level.goorm.io/exam/43225/코드-돈이-급한-남자/quiz/1

n = int(input())
works = {}

for _ in range(n):
    time, pay = map(int, input().split())
    works.setdefault(time, pay)
    if works[time] < pay:
        works[time] = pay

print(sum(works.values()))