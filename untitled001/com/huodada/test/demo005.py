#!/usr/bin/python
# _*_ coding: UTF-8 _*_
# 输入三个整数x，y，z，请把这三个数由小到大输出。
from pip._vendor.distlib.compat import raw_input

l = []
for i in range(3):
    x = int(raw_input('integer:\n'))
    l.append(x)
l.sort()
print(l)
