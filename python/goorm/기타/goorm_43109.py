# goorm / 기타 / 배드민턴 경기
# https://level.goorm.io/exam/43109/%EC%BD%94%EB%93%9C-%EB%B0%B0%EB%93%9C%EB%AF%BC%ED%84%B4-%EA%B2%BD%EA%B8%B0/quiz/1

ch = list(map(int, input().split()))
ko = list(map(int, input().split()))

ch.sort()
ko.sort()

cnt = 0
while len(ch) > 0:
    for k in ko:
        if ch[0] <= k:
            cnt += 1
            ko.remove(k)
            break
    ch.pop(0)

print(cnt)