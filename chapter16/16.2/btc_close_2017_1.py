#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from urlib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json
import requests
import pygal
import math
from itertools import groupby


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_requests.json', 'w') as f:
    f.write(req.text)
# 加载json格式
file_requests = req.json()

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in file_requests:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], close[:idx_month], '收盘价月日均值（¥）', '月日均值')
