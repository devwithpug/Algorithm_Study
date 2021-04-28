# goorm / 기타 / 369 게임
# https://level.goorm.io/exam/48757/369-%EA%B2%8C%EC%9E%84/quiz/1

n = int(input())

answer = 0
for i in range(n):
    answer += str(i).count('3') + str(i).count('6') + str(i).count('9')
    
print(answer)