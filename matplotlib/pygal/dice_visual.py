#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from die import Die
import pygal

# 创建两个D6骰子
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []

times = 5000

for roll_num in range(times):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []

for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对数据进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling 'D%d' + 'D%d' %d times" % (
    die_1.num_sides, die_2.num_sides, times)
hist.x_labels = [str(x)
                 for x in range(2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

# 添加图例
hist.add('D6', frequencies)

# 渲染到文件
hist.render_to_file('die_visual.svg')
