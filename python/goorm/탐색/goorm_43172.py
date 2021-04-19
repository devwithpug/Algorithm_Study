# goorm / 탐색 / 평형 저울
# https://level.goorm.io/exam/43172/%ED%8F%89%ED%98%95-%EC%A0%80%EC%9A%B8/quiz/1

def dfs(items, a, b, result):
    if sum(a) == sum(b):
        result.append(a+[0]+b)
    if len(items) != 0 and len(result)==0:
        for i in items:
            nxt_items = items[:]
            nxt_items.remove(i)
            nxt_a = a[:]
            nxt_a.append(i)
            dfs(nxt_items[:], nxt_a[:], b[:], result)
            nxt_b = b[:]
            nxt_b.append(i)
            dfs(nxt_items[:], a[:], nxt_b[:], result)

items = [1, 3, 7, 26, 94, 259]
n = int(input())
result = []
answer = dfs(items, [n], [], result)

if len(result) == 0:
    print(n, end=" ")
else:
    for a in sum(result,[]):
        print(a, end=" ")