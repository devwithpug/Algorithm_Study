# goorm / 정렬 / 오늘의 업무
# https://level.goorm.io/exam/43205/%EC%98%A4%EB%8A%98%EC%9D%98-%EC%97%85%EB%AC%B4/quiz/1

n, r = map(int, input().split())
arr = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}

for _ in range(r):
    a, b = map(str, input())
    if arr[a] > arr[b]:
        arr[a], arr[b] = arr[b], arr[a]
    
for i in range(n):
    for key, item in arr.items():
        if i == item:
            print(key, end="")
            
            
# DFS를 이용한 위상정렬 공부하기
#UNSOLVED