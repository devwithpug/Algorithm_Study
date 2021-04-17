# goorm / 탐색 / 회사 가는 길
# https://level.goorm.io/exam/43270/%ED%9A%8C%EC%82%AC-%EA%B0%80%EB%8A%94-%EA%B8%B8/quiz/1

def dfs(dic, visit, st, ed, cost, result):
    if st == ed:
        result.append(cost)
        return
    visit[st-1] = True
    for to, cst in dic[st]:
        if not visit[to-1]:
            dfs(dic, visit[:], to, ed, cost+cst, result)

a, b = map(int, input().split())
visit = [False] * a
dic = {}
result = []

for _ in range(b):
    st, ed, cost = map(int, input().split())
    dic.setdefault(st, [])
    dic.setdefault(ed, [])
    dic[st].append([ed, cost])
    dic[ed].append([st, cost])
    
dfs(dic, visit[:], 1, a, 0, result)

print(min(result))
