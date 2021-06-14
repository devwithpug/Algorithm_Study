# goorm / 기타 / 자동화 로봇
# https://level.goorm.io/exam/43070/1e-자동화-로봇/quiz/1
# 시간 초과

def do(jobs):
    queue = []
    day = 1
    while len(jobs) > 0 or len(queue) > 0:

        hours = 8
        # 시작 가능한 job들 push
        for _ in range(len(jobs)):
            si, ei, wi = jobs.pop(0)
            if si == day:
                queue.append((si, ei, wi))
            else:
                jobs.append((si, ei, wi))
                jobs.sort(key=lambda x: x[0])
        # ei 낮은 순서로 queue 정렬
        queue.sort(key=lambda x: x[1])
        # job 실행
        while len(queue) > 0 and hours > 0:
            si, ei, wi = queue.pop(0)
            if day > ei:
                return False
            if wi > hours:
                wi -= hours
                hours = 0
                queue.append((si, ei, wi))
            else:
                hours -= wi
        day += 1
    return True


t = int(input())
answer = []
for _ in range(t):

    n = int(input())
    jobs = []
    for _ in range(n):
        jobs.append(tuple(map(int, input().split())))

    jobs.sort(key=lambda x: x[0])
    answer.append(do(jobs))

for a in answer:
    if a:
        print("Yes")
    else:
        print("No")

