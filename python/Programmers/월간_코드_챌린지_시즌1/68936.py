# https://programmers.co.kr/learn/courses/30/lessons/68936

def search(answer, arr, size, x, y):
    if arr[y][x] == -1:
        return
    
    compress = list(set(sum([row[x:x+size] for row in arr[y:y+size]], [])))
    
    if len(compress) == 1:
        for yy in range(y, y+size):
            for xx in range(x, x+size):
                arr[yy][xx] = -1
        answer[compress[0]] += 1

def solution(arr):
    
    answer = [0, 0]
    size = len(arr)
    
    while size > 0:
        
        line = 0
        y = 0
        x = 0
        
        for _ in range(0, len(arr)**2 // size, size):
            
            search(answer, arr, size, x//size*size, y*size)

            x += size
            line += 1
            if line == len(arr) // size:
                x = 0
                y += 1
                line = 0

        size = int(size/2)

    return answer

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))
