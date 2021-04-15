# goorm / 탐색 / (코드)울타리 자르기
# https://level.goorm.io/exam/43102/%EC%BD%94%EB%93%9C-%EC%9A%B8%ED%83%80%EB%A6%AC-%EC%9E%90%EB%A5%B4%EA%B8%B0/quiz/1
# 시간복잡도 때문에 divide and conquer로 해결

# dfs의 경우 시간초과 발생 가능 O(n^2)
def dfs(now, arr, width, result):
    if now>arr[0]:
        result.append(now*width)
        now = arr[0]
    if len(arr)==1:
        if now <= arr[0]:
            result.append(now*(width+1))
        else:
            result.append(now*(width))
        return    
    for i in range(1, now+1):
        dfs(i, arr[1:], width+1, result)
    if now<arr[0]:
        for i in range(now+1, arr[0]+1):
            dfs(i, arr[1:], 1, result)

# divide and conquer
# O(n log n)
def binary_search(arr, a, b):
    if a == b:
        return arr[a]
    mid = int((a+b)/2)
    answer = max(binary_search(arr, a, mid), binary_search(arr, mid+1, b))
        
    l = mid
    r = mid+1
    h = min(arr[l], arr[r])
    answer = max(answer, 2 * h)
    
    while l > a or r < b:
        if r < b and (l == a or arr[r+1] > arr[l-1]):
            r += 1
            h = min(h, arr[r])
        else:
            l -= 1
            h = min(h, arr[l])
        answer = max(answer, (r-l+1) * h)
    return answer

n = int(input())
arr = list(map(int, input().split()))

print(binary_search(arr, 0, n-1))

# result = []
# dfs(arr[0], arr[1:], 1, result)
# print(max(result))