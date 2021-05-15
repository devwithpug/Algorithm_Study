# goorm / 기타 / 채점하기
# https://level.goorm.io/exam/43280/%EC%B1%84%EC%A0%90%ED%95%98%EA%B8%B0/quiz/1

target = list(input())

score = 0
answer = 0
for a in target:
    if a == 'o':
        score += 1
        answer += score
    else:
        score = 0

print(answer)