# goorm / 정렬 / 홀수 놀이
# https://level.goorm.io/exam/43127/%ED%99%80%EC%88%98-%EB%86%80%EC%9D%B4/quiz/1

n = int(input())

odd = []

for i in range(10000000):
    if i % 2 != 0:
        odd.append(i)

s = sum(odd[:n-1])
l = sum(odd[:n])
print(sum(odd[s:l][-3:]))