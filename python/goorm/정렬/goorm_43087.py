# goorm / 정렬 / 세로 읽기
# https://level.goorm.io/exam/43087/%EC%84%B8%EB%A1%9C-%EC%9D%BD%EA%B8%B0/quiz/1

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(str, input().split())))
    
for x in range(n-1, -1, -1):
    for y in range(n):
        print(arr[y][x], end="")