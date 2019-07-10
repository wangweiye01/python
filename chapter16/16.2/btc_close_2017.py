#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from urlib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_requests.json', 'w') as f:
    f.write(req.text)
# 加载json格式
file_requests = req.json()

for btc_dict in file_requests:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))