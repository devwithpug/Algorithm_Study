# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum(map(lambda x, y: x*y, a, b))

a = [1,2,3,4]
b = [-3,-1,0,2]

print(solution(a,b))