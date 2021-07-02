# https://programmers.co.kr/learn/courses/30/lessons/67257

def calc(op, x, y):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    else:
        return x*y


def dfs(orders, nums, ops):
    i = 0
    while len(ops) > 0:
        j = 0
        
        while orders[i] in ops:
            if orders[i] == ops[j]:
                nums.insert(j, calc(ops.pop(j), nums.pop(j), nums.pop(j)))
                j -= 1
            j += 1
        i += 1
    return abs(nums[0])


def solution(expression):
    answer = 0
    num = ""
    nums = []
    ops = []
    orders = [
        ('-', '+', '*'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('+', '*', '-'),
        ('*', '-', '+'),
        ('*', '+', '-'),
    ]
    for i in expression:
        if i in ('+', '-', '*'):
            nums.append(int(num))
            num = ""
            ops.append(i)
        else:
            num += i
    nums.append(int(num))

    for order in orders:
        answer = max(answer, dfs(order, nums[:], ops[:]))

    return answer


expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(solution(expression))
