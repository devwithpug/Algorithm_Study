# goorm / 기타 / 문자열 번갈아 출력하기
# https://level.goorm.io/exam/43110/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B2%88%EA%B0%88%EC%95%84-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0/quiz/1

target = list(input())

while len(target)>0:
    print(target.pop(0), end="")
    if len(target)==0:
        break
    print(target.pop(-1), end="")