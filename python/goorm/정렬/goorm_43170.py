# goorm / 정렬 / 유일한 수
# https://level.goorm.io/exam/43170/%EC%9C%A0%EC%9D%BC%ED%95%9C-%EC%88%98/quiz/1

n = int(input())

arr = list(map(int, input().split()))
queue = []

for a in arr:
    if a in queue:
        queue.remove(a)
    else:
        queue.append(a)
        
print(queue[0])