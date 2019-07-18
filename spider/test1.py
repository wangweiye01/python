#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

url = "http://www.guan18.com"
a = urllib.request.urlopen(url)
print(a.getcode())
data = a.read()
data = data.decode('UTF-8')
print(data)