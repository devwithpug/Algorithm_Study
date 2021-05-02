# goorm / 정렬 / 오늘의 업무
# https://level.goorm.io/exam/43205/%EC%98%A4%EB%8A%98%EC%9D%98-%EC%97%85%EB%AC%B4/quiz/1
# 위상정렬 알고리즘

n, r = map(int, input().split())
arr = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
path = {}
queue = []

for i in range(n):
    path.setdefault(arr[i], [])
    queue.append(arr[i])

for _ in range(r):
    a, b = map(str, input())
    path[b].append(a)

print(path)

while len(queue) > 0:
    for item in queue:
        if len(path[item]) > 0:
            continue
        for k in path.keys():
            if item in path[k]:
                path[k].remove(item)
        print(item, end="")
        queue.remove(item)
        break