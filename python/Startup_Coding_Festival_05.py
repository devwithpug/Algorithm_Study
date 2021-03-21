# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# SOLVED

size = int(input())
matrix = []
result = []

def PP(list_2d, m):
    total = 0
    for line in list_2d:
        total += sum(line)
    if total == m*m:
        return True
    else:
        return False
    

for i in range(size):
    st = list(map(int, input()))
    matrix.append(st)
for m in range(1,size+1):
    tmp = 0
    
    for x in range(size+1-m):
        for y in range(size+1-m):
            tmp = tmp + 1 if PP([row[y:y+m] for row in matrix[x:x+m]], m) else tmp
    result.append(tmp)
    
print("total: {}".format(sum(result)))
for m in range(0, size):
    if result[m] > 0:
        print("size[{}]: {}".format(m+1, result[m]))
    
                