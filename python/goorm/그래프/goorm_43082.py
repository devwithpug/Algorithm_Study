# goorm / 그래프 / 최단 거리 구하기
# https://level.goorm.io/exam/43082/최단-거리-구하기/quiz/1
# bfs search

n = int(input())

path = []
dp = []
for y in range(n):
    path.append(list(map(int, input().split())))
    dp.append([0]*n)

queue = [(0, 0)]
dp[0][0] = 1

def search(y, x, path, dp, queue, value):
    if path[y][x] == 1:
        queue.append((y, x))
        if dp[y][x] < value + 1:
            path[y][x] = 0
        dp[y][x] = value+1 if dp[y][x] == 0 else min(value + 1, dp[y][x])

while len(queue) != 0:
    
    y, x = queue.pop(0)
    if y == n-1 and x == n-1:
        break
    if y-1 >= 0:
        search(y-1, x, path, dp, queue, dp[y][x])
    if y+1 < n:
        search(y+1, x, path, dp, queue, dp[y][x])
    if x-1 >= 0:
        search(y, x-1, path, dp, queue, dp[y][x])
    if x+1 < n:
        search(y, x+1, path, dp, queue, dp[y][x])

print(dp[n-1][n-1])