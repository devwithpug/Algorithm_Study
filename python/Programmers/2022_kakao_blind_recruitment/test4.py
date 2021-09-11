# 2022 KAKAO BLIND RECRUITMENT test_4 solved

SCORE = [10,9,8,7,6,5,4,3,2,1,0]

def do_score(answer, n ,info, i, score, left, tries):
    if left == 0 or 10 == i:
        score_a = 0
        for i in range(10):
            if info[i] > tries[i]:
                score_a += SCORE[i]

        result = score - score_a
        if answer[1] <= result:
            if sum(tries) != n:
                tries[10] = n - sum(tries)
            chk = True
            if answer[1] == result:
                if answer[1] > 0:
                    for i in range(10, -1, -1):
                        if answer[0][i] > 0 and tries[i] == 0:
                            chk = False
                            break
                        elif answer[0][i] == 0 and tries[i] > 0:
                            break
            if chk:
                answer.clear()
                answer.append(tries)
                answer.append(result)
        
    else:
        scored = tries[:]
        scored[i] = info[i]+1
        
        do_score(answer, n, info, i+1, score+SCORE[i], left-info[i]-1, scored[:]) if info[i] < left else 0
        do_score(answer, n, info, i+1, score, left, tries[:])


def solution(n, info):
    answer = [[], 0]
    tries = [0] * 11
    do_score(answer, n, info, 0, 0, n, tries[:])
    return answer[0] if answer[1] > 0 else [-1]


# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

# print(solution(n, info))

# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# print(solution(n, info))

# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]

# print(solution(n, info))
# n = 2
# info = [2,0,0,0,0,0,0,0,0,0,0]

# print(solution(n, info))

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))
