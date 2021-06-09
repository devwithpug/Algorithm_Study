# goorm / 스택,큐 / N Queen's Problem
# https://level.goorm.io/exam/43150/n-queen-s-problem/quiz/1

def is_possible(matrix, row):
    for i in range(row):
        if matrix[i] == matrix[row]:
            return False
        if abs(matrix[i] - matrix[row]) == abs(i - row):
            return False
    return True

def search(matrix, row, n, answer):
    if row == n:
        answer.append(1)
        return

    for i in range(n):
        matrix[row] = i
        if is_possible(matrix, row):
            search(matrix, row+1, n, answer)

n = int(input())
matrix = [0] * n
answer = []

search(matrix, 0, n, answer)
print(sum(answer))