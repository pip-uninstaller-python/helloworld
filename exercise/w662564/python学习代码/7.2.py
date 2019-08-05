# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/3 18:46
# @Author  : 錵滊嫣缘
# @File    : 7.2.py
# @Software: PyCharm

# 设计一个装饰器，他可以作用于任何函数上，打印函数执行的时间
import time
# 创建一个装饰器
def time_value(fn):
    def wrapper(*args,**kwargs):
        # 程序运行开始计时
        start_time = time.time()
        # 接受函数
        get_str = fn(*args,**kwargs)
        # 程序结束计时
        end_time = time.time()
        print("函数运行共耗时：{:0.4f}s".format(end_time-start_time))
        # 返回函数
        return get_str
    return wrapper
@time_value
def test():
    i = 0
    while i < pow(2,22):
        i += 1
    return i
print(test())
