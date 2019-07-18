#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib
import random

from collections import deque


def saveFile(data, filename):
    save_path = '/Users/wangweiye/t/' + filename
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()


queue = deque()
visited = set()

url = 'http://www.zhihu.com'  # 入口页面，可以换成别的


queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    visited |= {url}

    print('已经抓取：' + str(cnt) + '  正在抓取<===  ' + url)
    cnt += 1

    try:
        urlop = urllib.request.urlopen(req, timeout=3)
    except:
        print('请求超时')
        continue

    if 'html' not in urlop.getheader('Content-Type'):
        continue

    # 避免程序异常终止，用try...catch处理异常
    try:
        data = urlop.read().decode()
    except:
        print('decode error')
        continue

    saveFile(data.encode(), str(random.random()) + '.html')

    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->' + x)
