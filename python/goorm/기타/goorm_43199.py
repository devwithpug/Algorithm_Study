# goorm / 기타 / 게임 마스터
# https://level.goorm.io/exam/43199/게임-마스터/quiz/1

total, win = map(int, input().split())
rate = int(win / total * 100)

i = 0
while total+i <= 1000000:
    if int((win+i) / (total+i) * 100) == rate + 1:
        break
    i += 1

print("X" if total+i >= 1000000 else i)