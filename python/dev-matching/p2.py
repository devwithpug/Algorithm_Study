# SOLVED

def solution(leave, day, holidays):
    answer = 0

    d = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    now = d.index(day)
    cal = []

    for i in range(1, 31):
        if i in holidays or d[now%7] in ['SAT', 'SUN']:
            cal.append(True)
            now+=1
        else:
            cal.append(False)
            now+=1

    print(cal)
    for i in range(30):
        ans = 0
        l = leave
        j = i
        while j < 30:
            if l == 0 and not cal[j]:
                break
            ans += 1
            if not cal[j]:
                l -= 1
            j += 1
        print(i, ans)
        answer = max(answer, ans)

    return answer


# print(solution(4, "FRI", [6,21,23,27,28]))
# print(solution(3, "SUN", [2,6,17,29]))
print(solution(30, "MON", [1,2,3,4,28,29,30]))