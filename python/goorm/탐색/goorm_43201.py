# goorm / 탐색 / 호프만 알고리즘
# https://level.goorm.io/exam/43201/%ED%98%B8%ED%94%84%EB%A7%8C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/quiz/1

n = int(input())
dic = {}

for _ in range(n):
    alpha, target = input().split()
    dic[target] = alpha

cipher = input()

answer = ""
tmp_str = ""
for c in cipher:
    tmp_str += c
    if tmp_str in dic.keys():
        answer += dic[tmp_str]
        tmp_str = ""

print(answer)