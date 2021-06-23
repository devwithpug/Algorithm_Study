# https://programmers.co.kr/learn/courses/30/lessons/67256

def get_pos(number, l_pos, r_pos):
    l_pos = 11 if l_pos == 0 else l_pos
    r_pos = 11 if r_pos == 0 else r_pos
    number = 11 if number == 0 else number

    l = abs(number - l_pos) // 3 + abs(number - l_pos) % 3
    r = abs(number - r_pos) // 3 + abs(number - r_pos) % 3 

    return (l, r)

def solution(numbers, hand):
    answer = ''
    l_pos = 10
    r_pos = 12
    
    for number in numbers:
        if number in [3,6,9]:
            answer += 'R'
            r_pos = number
        elif number in [1,4,7]:
            answer += 'L'
            l_pos = number
        else:
            l, r = get_pos(number, l_pos, r_pos)
            if l == r:
                if hand == 'left':
                    answer += 'L'
                    l_pos = number
                else:
                    answer += 'R'
                    r_pos = number
            elif l < r:
                answer += 'L'
                l_pos = number
            else:
                answer += 'R'
                r_pos = number

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = solution(numbers, hand)
print(result)