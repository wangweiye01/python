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

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]

close_log = [math.log10(_) for _ in close]

line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价折线图（￥）.svg')