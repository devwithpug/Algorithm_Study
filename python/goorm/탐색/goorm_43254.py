# goorm / 탐색 / 암벽등반
# https://level.goorm.io/exam/43254/%EC%95%94%EB%B2%BD%EB%93%B1%EB%B0%98/quiz/1

def reachable(n, x, y):
    return 0 <= x and x < n and 0 <= y and y < n
    
def dfs(result, path, visit, x, y, hp):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(path)
    visit[n*y+x] = True
    if int(n*n*0.75) == visit.count(True):

        result.append(hp)
        return
    for i in range(4):
        if reachable(n, x+dx[i], y+dy[i]) and not visit[n*(y+dy[i]) + (x+dx[i])]:
            if path[x][y] == path[x+dx[i]][y+dy[i]]:
                dfs(result, path, visit[:], x+dx[i], y+dy[i], hp)
            else:
                dfs(result, path, visit[:], x+dx[i], y+dy[i], max(hp, abs(path[x][y] - path[x+dx[i]][y+dy[i]])))
    
n = int(input())
path = []
visit = [False] * (n*n)
result = []

for _ in range(n):
    path.append(list(map(int, input().split())))
if n != 0:
    for x in range(0, int(n/2)+1):
        for y in range(0, int(n/2)+1):
            dfs(result, path, visit[:], x, y, 0)
        
if len(result) == 0:
    print(0)
else:
    print(min(result))
