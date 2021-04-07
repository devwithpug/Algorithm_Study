# goorm / 탐색 / 요일 구하기
# https://level.goorm.io/exam/43137/%EC%9A%94%EC%9D%BC-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

month, day = map(int, input().split())
str_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month_day = [31,29,31,30,31,30,31,31,30,31,30,31]

total = sum(month_day[:month-1]) + day - 1
if month in range(1,13) and day in range(1, month_day[month-1]+1):
    print(str_day[(5+total) % 7])
else:
    print("ERROR")