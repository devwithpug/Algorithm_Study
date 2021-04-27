# goorm / 정렬 / 뱀 유리수 수열
# https://level.goorm.io/exam/43220/%EB%B1%80-%EC%9C%A0%EB%A6%AC%EC%88%98-%EC%88%98%EC%97%B4/quiz/1

"""
1/1 1/2 2/1 3/1 2/2 1/3
"""

n = int(input())

i, j, k = 1, 1, 1    

while n > k:
    j += 1
    k += 1
    if k == n:
        break
    while j > 1 and n > k:
        j -= 1
        i += 1
        k += 1
    if k == n:
        break
    i += 1
    k += 1
    if k == n:
        break
    while i > 1 and n > k:
        i -= 1
        j += 1
        k += 1

print("{}/{}".format(i, j))


