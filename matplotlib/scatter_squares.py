#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40, edgecolor='none',
            c=y_values, cmap=plt.cm.Blues)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)

plt.axis([0, 1100, 0, 1100000])
plt.show()

# 保存图标到文件
# plt.savefig('squares_plot.png', bbox_inches='tight')
