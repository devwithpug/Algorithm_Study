# 2022 KAKAO BLIND RECRUITMENT test_3 solved

import math

def calc_time_diff(curr, prev):
    curr = curr.split(":")
    prev = prev.split(":")

    h = int(curr[0]) - int(prev[0])
    m = int(curr[1]) - int(prev[1])

    return (h*60) + m

def solution(fees, records):
    answer = []
    mins = {}
    status = {}
    times = {}
    for r in records:
        t, n, s = r.split(" ")
        mins.setdefault(n, 0)
        status.setdefault(n, '')
        times.setdefault(n, '')

        if status[n] == 'IN' and s == 'OUT':
            mins[n] += calc_time_diff(t, times[n])
        else:
            times[n] = t
        status[n] = s
        
    for k, v in status.items():
        if v == 'IN':
            mins[k] += calc_time_diff('23:59', times[k])
    
    for n, m in sorted(mins.items()):
        if m > fees[0]:
            charge = fees[1] + math.ceil((m-fees[0]) / fees[2]) * fees[3]
        else:
            charge = fees[1]
        answer.append(charge)

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))