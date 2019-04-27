#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()
print(now)

dt = datetime(2019, 4, 19, 12, 22)
print(dt)

# 将datetime类型转换成timestamp
t = dt.timestamp()
print(t)

# 将timestamp转换成datetime类型
print('将timestamp转换成datetime类型:', datetime.fromtimestamp(t))

# 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。本地时间是指当前操作系统设定的时区

# timestamp转换成UTC标准时区时间
print('UTC时间:', datetime.utcfromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减