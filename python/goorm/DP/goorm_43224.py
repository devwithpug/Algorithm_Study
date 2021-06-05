# goorm / DP / 멀티탭 스케쥴링
# https://level.goorm.io/exam/43224/멀티탭-스케줄링/quiz/1

n, k = map(int, input().split())

cnt = {}
use = list(map(int, input().split()))
queue = []
answer = 0

for item in use:
    cnt.setdefault(item, 0)
    cnt[item] += 1

for i in use:
    if len(queue) != n:
        queue.append(i)
    else:
        if not i in queue:
            minimum_usage = queue[0]
            for q in queue:
                if cnt[minimum_usage] > cnt[q]:
                    minimum_usage = q
            queue.remove(minimum_usage)
            queue.append(i)
            answer += 1

print(answer)
