from lxml import etree
import requests

# lxml库继承了libxml2的特性，具有自动修正HTML代码的功能，还添加了<html>和<body>标签
# etree: html转为element对象

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}   # 加入请求头

# 遇到相同字符开头的多个标签，使用starts-with()可以获取多个标签内容
# 遇到嵌套情况，用string(.)方法
html = '''
<li class="tag-1">需要的内容1</li>
<li class="tag-2">需要的内容2</li>
<li class="tag-3">需要的内容3</li>
'''
selector = etree.HTML(html)
contents = selector.xpath('//li[starts-with(@class,"tag")]/text()')
for content in contents:
    print(content)  # 可获取类似标签的信息
# 遇到标签嵌套的情况时
html2 = '''
<div class="red">需要的内容1
    <h1>需要的内容2</h1>
</div>
'''
selector2 = etree.HTML(html2)
content1 = selector2.xpath('//div[@class="red"]')[0]
content2 = content1.xpath('string(.)')  # string(.)方法可用于标签嵌套情况
print(content2)


# # 获取糗事百科页面id信息
# url = 'http://www.qiushibaike.com/text/'
# res = requests.get(url, headers=headers)
# selector = etree.HTML(res.text)
# url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
# url_infoss = selector.xpath('//div[@class="article block untagged mb15 typs_long"]')
# url_infosss = selector.xpath('//div[@class="article block untagged mb15 typs_old"]')
# url_infos.extend(url_infoss)
# url_infos.extend(url_infosss)
# for url_info in url_infos:
#     if url_info.xpath('div[1]/a[2]/h2/text()'):
#         id = url_info.xpath('div[1]/a[2]/h2/text()')[0]
#         print(id)
#     else:
#         pass


# url = 'http://www.qiushibaike.com/text/'
# res = requests.get(url, headers=headers)
# selector = etree.HTML(res.text)
# # 返回列表的数据结构
# id = selector.xpath('//*[@id="qiushi_tag_121312492"]/div[1]/a[2]/h2/text()')[0]
# print(id)


# res = requests.get('http://ww.biaud.com/', headers=headers)
# html = etree.HTML(res.text)
# result = etree.tostring(html)
# print(result)


# html = etree.parse('flower.html')
# result = etree.tostring(html, pretty_print=True)
# print(result)


# text = '''
# <div>
#     <ul>
#         <li class="red"><h1>red flowers</h1></li>
#         <li class="yellow"><h2>yellow flowers</h2></li>
#         <li class="white"><h3>white flowers</h3></li>
#         <li class="black"><h4>black flowers</h4></li>
#         <li class="blue"><h5>blue flowers</h5></li>
#     </ul>
# </div>
# '''
#
# html = etree.HTML(text)
# print(html)  # lxml库解析数据，为Element对象
#
# result = etree.tostring(html)
# print(result)  # lxml库解析可自动修正html

