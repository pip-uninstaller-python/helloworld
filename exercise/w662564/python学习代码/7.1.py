# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 18:50
# @Author  : 錵滊嫣缘
# @File    : 7.1.py
# @Software: PyCharm

class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        # 每次实例化就把count+1
        Student.count+=1
if __name__ == '__main__':
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaohong = Student('红')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaolv = Student('小绿')
    xiaohong = Student('红')
    print(Student.count)
