#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('100 + 200 + 300 =', 100 + 200 + 300)

name = input("please input your name: ")

print("Hello world", name)

a = 100
if a >=0:
    print("大于0")
else:
    print("小于0")


print(3 > 2)

# 常量用全部大写变量名来标识，但是Python没有机制保证PI值不能被改变，只是一种习惯而已
PI = 3.1415926

# 除法
print("除法:", 10 / 3)

# 地板除
print("地板除:", 10 // 3)

# 余数
print("余数:", 10 % 3)

# Python3中编码是以Unicode编码的.ord()获取字符的编码值,chr()把编码转换成字符
print(ord('A'))

print(ord('B'))

# 格式化
print('Hello, %s, you have $%d' % ('wangweiye', 900))

# 有序列表
classmates = ['John', 'Jack', 110]
print('班里有学生%d个' % len(classmates))

# 获得最后一个学生
print('最后一个学生是:%s' % classmates[-1])

# 新来一个学生
classmates.append('Sisi')

# 元组(tuple)，元组指向不可变化

classmates1 = (1, 2, ['John', 'Jack'])

classmates1[2][0] = 'X'

print(classmates1[2][0])

# 循环
for classmate in classmates1:
    print(classmate)

sum = 0

ele = range(101)

for e in ele:
    sum = sum + e
print('和为:%d' % sum)

# dict(相当于Java中的map)

d = {'Michael': 90, 'John': 89}
print('Michael的得分是:', d['Michael'])

print('John' in d)
print(d.get('Lisa'))
print(d.get('Lisa', -1))

# 删除
print(d.pop('John'))

# set集合
s1 = set([1, 1, 2, 2, 3, 3])
s1.add(4)
s1.remove(1)
# 交集
s2 = set([4, 6])
print(s1 & s2)
# 并集
print(s1 | s2)



# 函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-1))

# 函数返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60)
print(r)

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

param = [2, 3, 1]
r =  calc(*param)

print(r)

# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}

# 简单方式调用
person('王伟业', 26, **extra)

# 丑笨方式调用
person('王伟业', 26, city = 'Beijing', job = 'Engineer')

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数
def person1(name, age, *, city='Shanghai', job='SaoDaJie'):
    print(name, age, city, job)

extra1 = {'city': 'Beijing', 'job': 'Engineer'}
person1('王伟业', 26, **extra1)

extra2 = {'city': 'Beijing'}
person1('王伟业', 26, **extra2)

# 使用切片实现trim
def trim(s):
    if s[:1] != '' and s[-1:] != '':
        return s
    elif s[:1] == '':
        return trim(s[1:])
    else:
        return trim(s[:-1])

print(trim(' sfsd fds '))
