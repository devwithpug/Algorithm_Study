# goorm / 기타 / 황제의 몰락
# https://level.goorm.io/exam/43266/%ED%99%A9%EC%A0%9C%EC%9D%98-%EB%AA%B0%EB%9D%BD/quiz/1

n, k = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]

target = 0
while len(arr) > 2:
    arr.pop(target)
    target = (target + k - 1) % len(arr)

print(' '.join(arr))