# goorm / 탐색 / 암호의 개수
# https://level.goorm.io/exam/43168/%EC%95%94%ED%98%B8%EC%9D%98-%EA%B0%9C%EC%88%98/quiz/1

a, b, n = map(int, input().split(" "))

answer = 0
for i in range(a,b+1):
    answer += pow(n, i)
    
print(answer)