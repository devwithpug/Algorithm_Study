# 월간 코드 챌린지 시즌 3 [10월] - 2번 문제 SOLVED

def solution(n, left, right):
    arr = []

    for i in range(left, right+1):
        if i+1 < n:
            arr.append(i+1)
        elif (i+1) % n == 0:
            arr.append(n)
        elif (i+1)%n <= i//n:
            arr.append(i//n+1)
        else:
            arr.append((i+1)%n)
    return arr



print(solution(3, 2, 5))
print(solution(10**7, 10**5, 10**6))
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 2 2 3 4 5

# 1 2 3 4
# 2 2 3 4
# 3 3 3 4
# 4 4 4 4

# 1 2 3 4 5 6 7     8   9 10  11  12  13  14  15  16
# 1 2 3 4 2 2 3     4   3 3   3   4   4   4   4   4


# 1 2 3
# 2 2 3
# 3 3 3

# 1 2 3 4 5 6 7 8 9
# 1 2 3 2 2 3 3 3 3
