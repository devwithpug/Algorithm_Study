# goorm / 기타 / 알파벳 빈도 구하기
# https://level.goorm.io/exam/43086/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EB%B9%88%EB%8F%84-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

line = list(input())

alpha = [0] * 200

for item in line:
    alpha[ord(item)] += 1

for i in range(ord("a"), ord("z")+1):
    print("{} : {}".format(chr(i), alpha[i-32] + alpha[i]))