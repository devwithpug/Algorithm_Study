# goorm / 탐색 / 소수의 개수 구하기
# https://level.goorm.io/exam/43096/%EC%86%8C%EC%88%98%EC%9D%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1
# 에라토스테네스의 채 알고리즘
# 시간복잡도 O(nloglogn)

def find_primes(n):
    arr = [True] * n
    
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i*2, n, i):
                arr[j] = False
    
    return len([_ for _ in range(2, n) if arr[_]])
    
    

n = int(input())
print(find_primes(n))
    
    