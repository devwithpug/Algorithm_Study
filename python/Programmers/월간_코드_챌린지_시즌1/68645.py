# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):

    arr = [[0] * i for i in range(1, n+1)]
    x, y, num = 0, -1, 1
    
    for i in range(1, n+1):

        for _ in range(n - i + 1):

            if i % 3 == 1:
                y += 1

            if i % 3 == 2:
                x += 1

            if i % 3 == 0:
                x -= 1
                y -= 1

            arr[y][x] = num
            num += 1
    
    return sum(arr, [])

print(solution(11))
