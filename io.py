#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 现代操作系统是不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据

# 读文件
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源
try:
    f = open('/Users/wangweiye/python/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 使用上述方法比较繁琐，可以使用with解决

with open('/Users/wangweiye/python/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

# 写文件

with open('/Users/wangweiye/python/test.txt', 'a', encoding = 'utf-8') as f:
    f.write('\nHello, world!')