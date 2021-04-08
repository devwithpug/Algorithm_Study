# goorm / 탐색 / 숫자 표현
# https://level.goorm.io/exam/43129/%EC%88%AB%EC%9E%90-%ED%91%9C%ED%98%84/quiz/1

n = int(input())

dic = {}

for i in range(1, n):
    dic.setdefault(i, [])
    for j in range(1, n+1):
        dic[i].append(j)

def dfs(dic, n, tmp, st, answer, result):
    if tmp == n:
        answer.append(result)
        return
    for v in dic[st]:
        if tmp+v <= n:
            tmp_result = result[:]
            tmp_result.append(v)
            dfs(dic, n, tmp+v, v, answer, tmp_result)
    return answer

items = []
for i in range(1, n):
    tmp = dfs(dic, n, i, 1, [], [i])
    for item in tmp:
        item.sort()
        if items.count(item) == 0:
            items.append(item)
    
print(len(items)+1)