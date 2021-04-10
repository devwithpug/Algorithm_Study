# goorm / 탐색 / 절단 가능 소수
# https://level.goorm.io/exam/43099/%EC%A0%88%EB%8B%A8-%EA%B0%80%EB%8A%A5-%EC%86%8C%EC%88%98/quiz/1
# dfs

import math

def is_prime(n):
    if (n<2):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def dfs(num, n):
    if not is_prime(int(num)):
        return
    if (len(num) > n):
        if is_prime(int(num)):
            print(num, end=" ")
        return
    for i in ['1','3','7','9']:
        dfs(num+i, n)

n = int(input())
        
for i in ['2','3','5','7']:
    dfs(i,n-1)