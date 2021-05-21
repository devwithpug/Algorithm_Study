# goorm / 기타 / 아메바
# https://level.goorm.io/exam/43193/%EC%95%84%EB%A9%94%EB%B0%94/quiz/1

n = int(input())
m, w = 0, 1
for _ in range(n):
    m, w = m+w, m+1
print(m, w)