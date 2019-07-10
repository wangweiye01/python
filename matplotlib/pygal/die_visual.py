#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from die import Die
import pygal

die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []

times = 1000

for roll_num in range(times):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对数据进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D%d %d times' % (die.num_sides, times)
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
