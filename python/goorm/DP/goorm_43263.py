# goorm / DP / 특정 구간의 합
# https://level.goorm.io/exam/43263/%ED%8A%B9%EC%A0%95-%EA%B5%AC%EA%B0%84%EC%9D%98-%ED%95%A9/quiz/1
# 문제가 DP랑 관련이 없음

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

print(sum(arr[a-1:b]))


# DP 이용하여 arr[0..n-1]인 배열에서 부분배열 최대합 찾기

def find(arr, n):
    max_ = 0
    partial = 0;
    
    for i in range(n):
        partial = max(0, partial) + arr[i]
        max_ = max(partial, max_)
        
    return max_