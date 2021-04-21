# goorm / 정렬 / 반복되는 숫자가 없는 수
# https://level.goorm.io/exam/43175/%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94-%EC%88%AB%EC%9E%90%EA%B0%80-%EC%97%86%EB%8A%94-%EC%88%98/quiz/1

def isDup(n):
    num = list(map(int, str(n)))
    for i in num:
        if num.count(i) > 1:
            return True
    return False

n = int(input())

result = []
i = 0
while len(result) != n:
    i += 1
    if isDup(i):
        continue
    result.append(i)
    
print(result[-1])