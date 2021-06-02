# goorm / JMOS
# https://level.goorm.io/exam/49109/jmos/quiz/1
# LIS 알고리즘 사용

def lis(seq):
    dp = [0] * len(seq)
    for i in range(1, len(seq)):
        _max = 0
        for j in range(i):
            if seq[i] > seq[j]:
                if _max < dp[j]:
                    _max = dp[j]
        dp[i] = _max+1            
    return max(dp)

n = int(input())
seq = list(map(int, input().split()))
seq = [0] + seq
print(n - lis(seq))