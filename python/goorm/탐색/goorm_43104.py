# goorm / 탐색 / 분해합
# https://level.goorm.io/exam/43104/%EB%B6%84%ED%95%B4%ED%95%A9/quiz/1
# brute force

num = int(input())
answer = 0

for i in range(int(str(num % pow(10, len(str(num))-1))[0]), num+1):
    numbers = [int(a) for a in str(i)]
    if i + sum(numbers) == num:
        answer = i
        break
print(answer)