# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import datetime

user_input = input()

time_table1 = []
time_table2 = []

for i in range(int(user_input)):
    s = input().split(" ")
    time_table1.append(datetime.datetime.strptime(s[0],'%H:%M'))
    time_table2.append(datetime.datetime.strptime(s[2],'%H:%M'))
    
out = datetime.datetime.strftime(max(time_table1), '%H:%M')
out2 = datetime.datetime.strftime(min(time_table2), '%H:%M')

if max(time_table1) > min(time_table2):
    print("-1")
else:
    print("{} ~ {}".format(out, out2))
