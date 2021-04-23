# goorm / 정렬 / Selection Sort
# https://level.goorm.io/exam/43265/selection-sort/quiz/1

n, step = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(step):
    min_index = i
    for j in range(i+1, n):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

for a in arr:
    print(a, end=" ")