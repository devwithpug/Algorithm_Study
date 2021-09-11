# 2022 KAKAO BLIND RECRUITMENT test_6
# 정확성 solved
# 효율성 unsolved

def solution(board, skill):
    answer = 0

    for s in skill:
        t, r1, c1, r2, c2, d = s

        for c in range(c1, c2+1):
            for r in range(r1, r2+1):
                if t == 1:
                    board[r][c] -= d
                else:
                    board[r][c] += d

    for l in board:
        for a in l:
            if a > 0:
                answer += 1

    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board, skill))