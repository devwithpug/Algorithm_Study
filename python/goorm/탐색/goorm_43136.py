# goorm / 탐색 / 삼각형 만들기
# https://level.goorm.io/exam/43136/%EC%82%BC%EA%B0%81%ED%98%95-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1
# 가장 큰 변의 길이 > 나머지 두변의 길이

n = int(input())
answer = 0

for i in range(1, int(n/3)+1):
    for j in range(int((n-i)/2), i-1, -1):
        if n-i-j < i+j:
            answer+=1
        
print(answer)