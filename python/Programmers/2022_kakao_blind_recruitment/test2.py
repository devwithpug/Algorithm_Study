# 2022 KAKAO BLIND RECRUITMENT test_2 solved

import math

N = '0123456789'

def change(num, base):
    q, r = divmod(num, base)
    return change(q, base) + N[r] if q else N[r]

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    if k < 10:
        n = change(n, k)
    else:
        n = str(n)

    lis = n.split('0')
    for a in lis:
        if a != '':
            if isPrime(int(a)):
                answer += 1

    return answer

n = 110011
k = 10
print(solution(n, k))
n = 437674
k = 3
print(solution(n, k))
