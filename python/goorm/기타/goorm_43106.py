# goorm / 기타 / 집합
# https://level.goorm.io/exam/43106/집합/quiz/1

n = int(input())

S = [False] * 20
answer = []
for _ in range(n):
    command = input().split()
    if command[0] == 'add':
        S[int(command[1])-1] = True
    elif command[0] == 'remove':
        S[int(command[1])-1] = False
    elif command[0] == 'check':
        answer.append(1 if S[int(command[1])-1] else 0)
    elif command[0] == 'all':
        S = [True] * 20
    elif command[0] == 'toggle':
        S[int(command[1])-1] = False if S[int(command[1])-1] else True
    elif command[0] == 'empty':
        S = [False] * 20

for item in answer:
    print(item)