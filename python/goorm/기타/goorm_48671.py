# goorm / 기타 / 통신비 계산하기
# https://level.goorm.io/exam/48671/%ED%86%B5%EC%8B%A0%EB%B9%84-%EA%B3%84%EC%82%B0%ED%95%98%EA%B8%B0/quiz/1

limit = {29900: 300, 34900: 1000, 39900: 2000, 49900: 6000, 59900: 11000, 69900: 100000}

order, used = map(int, input().split())
if used > limit[order]:    
    over = used - limit[order]
    value = max(min(180000, over * 20), order) if over >= 5000 else min(25000, over * 20)
else:
    value = 0

min_order = order
min_value = value
for k, v in limit.items():
    if used > limit[k]:
        tmp_over = used - limit[k]
        tmp_value = max(min(180000, tmp_over * 20), k) if tmp_over >= 5000 else min(25000, tmp_over * 20)
    else:
        tmp_value = 0
    if k + tmp_value < min_order + min_value:
        min_order, min_value = k, tmp_value
    
print(min_order, order + value, min_order+min_value)