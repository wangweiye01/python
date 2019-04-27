#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
print(os.name)
print(os.uname())

# 环境变量
print(os.environ)

# 获得某个环境变量的值
print(os.environ.get('PATH'))
print('\n')

# 操作文件和目录

# 查看当前目录的绝对路径
print('当前目录的绝对路径是:', os.path.abspath('.'))

# 创建新的目录
if os.path.exists('/Users/wangweiye/python/newdir') == False:
    os.mkdir('/Users/wangweiye/python/newdir')

if os.path.exists('/Users/wangweiye/python/newdir'):
    os.rmdir('/Users/wangweiye/python/newdir')

# 将两个路径合成一个时，不要直接拼接字符串，而要通过os.path.join()函数，这样可以处理不同操作系统的路径分隔符
print(os.path.join('/Users/wangweiye/python', 'newfir'))
# 同样道理，拆分路径时，也不要直接去拆字符串
print(os.path.split('/Users/wangweiye/python/file.txt'))
# 获得文件扩展名
print(os.path.splitext('/Users/wangweiye/python/file.txt')[1])

print(os.listdir('.'))
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def find_file(str, path = '.'):
    dir = os.listdir('.')
    for d in dir:
        current = os.path.join(path, d)
        if os.path.isdir(d):
            find_file(str, current)
        elif d.find(str) > -1:
            print(current)

find_file('io')