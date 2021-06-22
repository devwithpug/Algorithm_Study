# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    depth = len(board)
    stack = []

    for x in moves:
        for y in range(depth):
            if board[y][x-1] != 0:
                target = board[y][x-1]
                board[y][x-1] = 0
                if len(stack) != 0 and stack[-1] == target:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(target)
                break
                
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

result = solution(board, moves)
print(result)