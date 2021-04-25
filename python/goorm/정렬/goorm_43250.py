# goorm / 정렬 / 배열 합치기
# https://level.goorm.io/exam/43250/%EB%B0%B0%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0/quiz/1

input()
arr = list(map(int, input().split()))
arr += list(map(int, input().split()))

arr.sort()
for a in arr:
    print(a, end=" ")