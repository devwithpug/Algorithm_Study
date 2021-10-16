# UNSOLVED

def beautify(arr):
    for a in arr:
        print(a)
    print()

def find(matrix):
    for i in range(6):
        for j in range(6):
            if matrix[i][j][0] > 0:
                if check(matrix, i, j, 0):
                    return True

def check(matrix, i, j, num):

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    matrix[i][j][1] = True

    for z in range(4):
        ii = i + dy[z]
        jj = j + dx[z]
        if ii >= 0 and ii < 6 and jj >= 0 and jj < 6:
            if matrix[i][j] == matrix[ii][jj] and not matrix[ii][jj][1]:
                print("recursion")
                return check(matrix, ii, jj, num+1)
    print("num",num)
    if num >= 3:
        return True
    else:
        return False
        
def pop(matrix):
    for i in range(6):
        for j in range(6):
            if matrix[i][j][1]:
                matrix[i][j] = [0, False]

def depop(matrix):
    for i in range(6):
        for j in range(6):
            matrix[i][j][1] = False



def solution(macaron):
    answer = []

    matrix = [[[0, False] for _ in range(6)] for _ in range(6)]

    beautify(matrix)

    for m in macaron:
        for i in range(-1, -7, -1):
            if matrix[i][m[0]-1][0] == 0:
                matrix[i][m[0]-1][0] = m[1]
                break
        if find(matrix):
            print("pop", m)
            pop(matrix)
        else:
            print("depop", m)
            depop(matrix)

        beautify(matrix)


    return answer



macaron = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]

print(macaron[-10])

print(solution(macaron))

# macaron = [[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]

# print(solution(macaron))

