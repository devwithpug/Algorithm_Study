# goorm / 기타 / 마라톤
# https://level.goorm.io/exam/43274/%EB%A7%88%EB%9D%BC%ED%86%A4/quiz/1

n = int(input())
speed = list(map(int, input().split()))
answer = []

for i in range(len(speed)):
    cnt = 1
    for j in range(i):
        if speed[i] < speed[j]:
            cnt += 1
    answer.append(str(cnt))
    
print(' '.join(answer))