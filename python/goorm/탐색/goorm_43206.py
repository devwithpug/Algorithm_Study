# goorm / 탐색 / 1, 2, 3
# https://level.goorm.io/exam/43206/1-2-3/quiz/1

def dfs(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return dfs(n-1) + dfs(n-2) + dfs(n-3)

n = int(input())

print(dfs(n))
