# goorm / 기타 / 상품 유통
# https://level.goorm.io/exam/43078/1b-상품-유통/quiz/1
# 부동소수점 오차로 인한 문제

def find(n):
    i = 1
    while str(n * i).split('.')[1] != '0':
        i += 1
    return i

t = int(input())
denom = []
num = []
for _ in range(t):
    n, r = map(int, input().split())
    tax = list(map(int, input().split()))
    for v in tax:
        r -= r * v / 100
    r = round(r, 10)
    f = find(r)

    num.append(r)
    denom.append(f)
    
for n, d in zip(num, denom):
    print("{}/{}".format(int(n*d), d))