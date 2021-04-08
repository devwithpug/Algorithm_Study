# goorm Binary search
# https://level.goorm.io/exam/43064/binary-search/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = input()
arr = input().split(" ")
k = input()


def binary_search(k, arr, a, b):
    if a > b:
        print("X")
        return
    mid = int((a + b) / 2)
    if int(arr[mid]) < int(k):
        binary_search(k, arr, mid + 1, b)
    elif int(arr[mid]) > int(k):
        binary_search(k, arr, a, mid - 1)
    elif arr[mid] == k:
        print(mid + 1)


binary_search(k, arr, 0, n - 1)
