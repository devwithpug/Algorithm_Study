# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# UNSOLVED

row , col = input().split()
row, col = (int(row), int(col))
matrix = []
table = str.maketrans('.xc', '012')

for c in range(col):
    matrix.append(input())
for c in range(col):
    matrix[c] = list(map(int, matrix[c].translate(table)))

start = []
for r in range(row):
    if matrix[0][r]== 2:
        start.append(r)

result = []
for s in start:
    tmp = 0
    for c in range(col):
        if matrix[c].count(0) == 0:
            tmp = -1
            break
        while matrix[c][s] == 1:
            tmp +=1
            if sum(matrix[c][:s]) < sum(matrix[c][s+1:]): # left
                if matrix[c][:s].count(0) == 0:
                    if matrix[c-1][s+1] == 1:
                        tmp = -1
                        break
                    s += 1
                    continue
                else:
                    if matrix[c-1][s-1] == 1:
                        tmp = -1
                        break
                    s -= 1
                    continue    
            else: # Right
                if matrix[c][s+1:].count(0) == 0:
                    if matrix[c-1][s-1] == 1:
                        tmp = -1
                        break
                    s -=1
                else:
                    if matrix[c-1][s+1] == 1:
                        tmp = -1
                        break
                    s += 1
    result.append(tmp)

print(min(result))
