# https://www.acmicpc.net/problem/5567

def dfs(answer, depth, f, target, check):
    if depth < 2:
        for nxt in f[target]:
            if not check[nxt-1] and nxt != 1:
                answer.append(nxt)
                check[nxt-1] = True
                dfs(answer, depth+1, f, nxt, check[:])

n = int(input())
m = int(input())
f = {}
check = [False] * n
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    f.setdefault(a, [])
    f.setdefault(b, [])
    f[a].append(b)
    f[b].append(a)

if 1 in f.keys():
    dfs(answer, 0, f, 1, check[:])

print(len(set(answer)))