# 월간 코드 챌린지 시즌 3 [10월] - 1번 문제 SOLVED

def solution(n):
    answer = n

    for i in range(1, n):
        if n % i == 1:
            answer = i
            break

    return answer


print(solution(10))
print(solution(12))
