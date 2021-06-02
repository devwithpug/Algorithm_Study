# goorm / DP / 파도반 수열
# https://level.goorm.io/exam/43272/파도반-수열/quiz/1

n = int(input())

arr = [0] * (n+1)

arr[0] = 1
arr[1] = 1
arr[2] = 1
for i in range(n-3):
    arr[i+3] = arr[i] + arr[i+1]

print(arr[n-1])