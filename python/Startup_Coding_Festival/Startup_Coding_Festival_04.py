# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# SOLVED

length = int(input())
line = input().split("0")

memo = [0 for _ in range(length+1)]

def dp(n):
    memo[0]=1
    memo[1]=1
    
    if n<2:
        return memo[n]
    
    for i in range(2, n+1):
        memo[i] = memo[i-2] + memo[i-1]
        
    return memo[n]

result = 1
for l in line:
    result *= dp(len(l)-1)
    
print(result)