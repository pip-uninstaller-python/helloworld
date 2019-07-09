#!/user/bin/python
# -*- coding: UTF-8 -*-
# import requests
# from bs4 import BeautifulSoup
# import requests

import requests
from lxml import etree
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头

f = open('F:/zhuanti.csv', 'a+', encoding='utf-8', newline='')
writer = csv.writer(f)
writer.writerow(('name', 'content', 'article', 'fans'))  # 写入csv头


def get_info(url):
    html = requests.get(url, headers=headers)  # 发送请求
    selector = etree.HTML(html.text)  # 解析页面
    infos = selector.xpath('//div[@class="col-xs-8"]')
    for info in infos:
        try:
            name = info.xpath('div/a[1]/h4/text()')[0]
            content = info.xpath('div/a[1]/p/text()')[0]
            article = info.xpath('div/div/a/text()')[0]
            fans = info.xpath('div/div/text()')[0]
            print(name, content, article, fans)
            writer.writerow((name, content, article, fans))
        except IndexError:
            pass


if __name__ == '__main__':
    urls = ['https://www.jianshu.com/recommendations/collections?page={}&order_by=hot'.format(str(i))
            for i in range(1, 5)]
    for url in urls:
        get_info(url)


# 字典
# x = {
#     1: 2,
#     2: 3
# }
# # print(x.get(3, 4))
# print(x.get(3, 4))

# # 小猪短租网
# res = requests.get('http://bj.xiaozhu.com/')
# print(res)
# print(res.text)


# 继承
# class Bike:
#     compose = ['frame', 'wheel', 'pedal']
#     def __init__(self):
#         self.other = 'basket'
#     def use(self, time):
#         print('you are riding {}m'.format(time*100))
# class Share_bike(Bike):
#     def cost(self,hour):
#         print('you spent {} hours'.format(hour*2))
# my_bike = Bike()
# my_bike.use(10)
# print(my_bike.other)
# bike = Share_bike()
# print(bike.other)
# bike.cost(2)

# 调用带参的方法和内置方法
# class Bike:
#     compose = ['frame', 'wheel', 'pedal']
#     def __init__(self):
#         self.other = 'basket'
#     def use(self, time):
#         print('you are riding {}m'.format(time*100))
# my_bike = Bike()
# my_bike.use(10)
# print(my_bike.other)

# class Bike:
#     compose = ['frame', 'whell', 'pedal']
# my_bike = Bike()
# my_bike.other = 'basket'
# your_bike = Bike()
# # 实例属性
# print(my_bike.other)
# print(my_bike.compose)
# print(your_bike.compose)

# 读取文件内容,每次关闭文件
# f = open("F:/file.txt", "r")
# content = f.read()
# print(content)
# f.close()
# 新建文件或打开文件写入
# f = open("F:/file.txt", "w+")
# f.write('Hello world!')

# 字符串的format方法
# urls = ["http://www.baidu.com/search-duanzufang-{}-0/".format(number)
# for number in range(1,14)]
# for url in urls:
#     print(url)

# a = b = c = 1
# print (a,b,c)
#
# cs = list()
# cs.append('Harry')
# cs.append('Love')
# cs.insert(0, 'first')
# # cs.pop(0)
# cs.remove('first')
# del cs[0]
# print (cs)
# print (cs[0])
# print (cs[-1])
#
# cs1 = ['cs0', 'cs1', 'cs2']
# cs.extend(cs1)
# print (cs)
#
# all = []
# print (all)
'''
 字典dictionary
 集合set
 元组tuple
 列表list
'''