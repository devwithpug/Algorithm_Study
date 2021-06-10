# goorm / 기타 / 어느 고고학자 이야기
# https://level.goorm.io/exam/43186/어느-고고학자-이야기/quiz/1

def check(n1, n2):
    if len(n1) >= len(n2)-len(n1):
        return False
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            return False
    return True


n = list(input())

p = 0
while True:
    num = 2**p
    if check(n, list(str(num))):
        print(p)
        break
    p += 1
