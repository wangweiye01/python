#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# 写入StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 读取StringIO
e = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = e.readline()
    if s == '':
        break
    print(s.strip())