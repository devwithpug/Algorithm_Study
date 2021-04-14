# goorm / 탐색 / 타일 채우기
# https://level.goorm.io/exam/43165/%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0/quiz/1
# dp로 해결
n, m = map(int, input().split())

dp = [0] * n
dp[0] = 1
dp[1] = 3
for i in range(2,n):
    dp[i] = (dp[i-1] + dp[i-2]*2)

print(dp[n-1] % m)
