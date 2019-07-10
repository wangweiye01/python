#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk的实例，并且将其包含的所有点都绘制出来
while True:
    rw = RandomWalk()
    rw.num_points = 50000
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')

    # 突出起点和终点(重绘起点和终点)
    plt.scatter(0, 0, c='green', edgecolor='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=10)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
