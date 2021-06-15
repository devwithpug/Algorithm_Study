# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

for i in range(int(user_input)):
    data = input().split(" ")
    N = int(data[0])
    M = int(data[1])
    
    k1 = int(N/5)
    k2 = int((N+M) / 12)
    k = k1 if k1<k2 else k2
    
    while N+M < 12*k:
        if k==0:
            break
        k -= 1
        
    print(k)
            