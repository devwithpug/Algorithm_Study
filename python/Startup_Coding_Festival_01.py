# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

user_input = input().split(" ")
arr = input().split(" ")

length = int(user_input[0])
k = int(user_input[1])

print(math.ceil((length - 1) / (k - 1)))

print(user_input)

min_num = min(arr)