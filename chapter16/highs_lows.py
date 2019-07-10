#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        int_high = int(row[1])
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        low = int(row[3])

        dates.append(current_date)
        highs.append(int_high)
        lows.append(low)
    
    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 填充两条线之间的空白区域
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置图形的格式
    plt.title("Daily hight and low temperatures - 2014", fontsize=24)
    plt.xlabel('Date', fontsize=6)
    # 绘制斜的日期标签，防止重叠
    fig.autofmt_xdate()

    plt.ylabel("Temperature(F)", fontsize=6)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()