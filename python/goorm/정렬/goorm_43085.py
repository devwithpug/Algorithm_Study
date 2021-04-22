# goorm / 정렬 / Insertion Sort
# https://level.goorm.io/exam/43085/insertion-sort/quiz/1
# 삽입정렬 시간복잡도 O(n^2)
int(input())
arr = list(map(int, input().split()))
n = int(input())

def selection_sort(arr, n):
    for i in range(n+1):
        tmp = arr[i]
        j = i - 1
        while arr[j] > tmp and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = tmp
    for a in arr:
        print(a, end=" ")
        
selection_sort(arr, n)