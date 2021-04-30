# goorm / DP / LIS(Longest Increasing Sequence)
# https://level.goorm.io/exam/43197/lis-longest-increasing-sequence/quiz/1

def lis(n, arr):
    first = [0] * (n+1)
    
    for i in range(n, -1, -1):
        first[i] = 1
        for j in range(i+1, n+1):
            if arr[j] > arr[i] and 1 + first[j] > first[i]:
                first[i] = 1 + first[j]
    return first[0] - 1

n = int(input())

arr = [-999]
arr += list(map(int, input().split()))

print(lis(n, arr))