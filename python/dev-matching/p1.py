# UNSOLVED

def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id

    registered_list.sort()
    registered_list.sort(key=len)

    print(registered_list)

    i = None
    for j in range(len(new_id)):
        if new_id[j].isdigit():
            i = j
            break

    S = new_id[:i]
    if i is None:
        i = len(new_id)
        N = 1
    else:
        N = int(new_id[i:])

    for a in registered_list:
        print(a, S)
        if not a.startswith(S):
            print("!!!",a, S)
            continue
        if a == new_id:
            continue
        if a != S+str(N):
            return S+str(N)
        N += 1
    return S+str(N)

print( 'gotoxy'.startswith('bird'))

def solution2(registered_list, new_id):

    if new_id not in registered_list:
        return new_id

    i = None
    while new_id in registered_list:
        if i is None:
            for j in range(len(new_id)):
                if new_id[j].isdigit():
                    i = j
                    break

        S = new_id[:i]
        if i is None:
            i = len(new_id)
            N = 0
        else:
            N = int(new_id[i:])

        new_id = S+ str(N+1)

    return new_id


print(solution(["abc", "abc1", "abc2", "abc3"], "abc"))
print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(["apple1", "orange", "banana3"], "apple"))
