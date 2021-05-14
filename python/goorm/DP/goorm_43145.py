# goorm / 기타 / 길찾기(다이아몬드)
# https://level.goorm.io/exam/43145/%EA%B8%B8%EC%B0%BE%EA%B8%B0-%EB%8B%A4%EC%9D%B4%EC%95%84%EB%AA%AC%EB%93%9C/quiz/1
# DP 알고리즘

n = int(input())
dp = []
matrix = []

for _ in range(n*2-1):
    line = list(map(int, input().split()))
    matrix.append(line)
    dp.append([0]*len(line))


for y in range(n*2-1):
    if y == 0:
        dp[0][0] = matrix[0][0]
    elif y < n:
        for x in range(y):
            dp[y][x] = max(dp[y][x], dp[y-1][x] + matrix[y][x])
            dp[y][x+1] = max(dp[y][x+1], dp[y-1][x] + matrix[y][x+1])    
    else:
        for x in range(n*2-y-1):
            dp[y][x] = matrix[y][x] + max(dp[y-1][x], dp[y-1][x+1])
        
print(dp[n*2-2][0])