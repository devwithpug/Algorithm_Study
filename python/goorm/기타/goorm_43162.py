# goorm / 기타 / Ugly Number
# https://level.goorm.io/exam/43162/ugly-number/quiz/1

n = int(input())
dp = [1]
i = 0
while i<n*10:
    if not dp[i] * 2 in dp:
        dp.append(dp[i] * 2)
    if not dp[i] * 3 in dp:
        dp.append(dp[i] * 3)
    if not dp[i] * 5 in dp:
        dp.append(dp[i] * 5)
    i += 1
dp.sort()
print(dp[n-1])