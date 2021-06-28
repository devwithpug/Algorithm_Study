# https://programmers.co.kr/learn/courses/30/lessons/77486

def sell(dic, answer, seller, value):
    to = int(value * 0.1)
    answer[seller] += value - to

    if dic[seller] != "-" and to > 0:
        sell(dic, answer, dic[seller], to)
        

def solution(enroll, referral, seller, amount):
    answer = {}
    dic = {}

    for e, r in zip(enroll, referral):
        dic[e] = r
        answer[e] = 0

    for s, a in zip(seller, amount):
        sell(dic, answer, s, a * 100)

    return [v for v in answer.values()]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))