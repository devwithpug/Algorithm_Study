# 2022 KAKAO BLIND RECRUITMENT test_1 solved

def solution(id_list, report, k):
    answer = []
    cnt = {}
    dic = {}

    for r in report:
        a, b = r.split(" ")
        dic.setdefault(a, [])

        if not b in dic[a]:
            dic[a].append(b)

            cnt.setdefault(b, 0)
            cnt[b] += 1

    keys = dic.keys()

    for id_ in id_list:
        tmp = 0
        if id_ in keys:
            for n in dic[id_]:
                if cnt[n] >= k:
                    tmp += 1
            answer.append(tmp)
        else:
            answer.append(0)

    return answer



id_ = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_, report, k))

id_ = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_, report, k))
