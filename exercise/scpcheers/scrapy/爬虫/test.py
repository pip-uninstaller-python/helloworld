import requests
from lxml import etree
from bs4 import BeautifulSoup
import re

# 测试selenium 和 PhantomJS
from selenium import webdriver
driver = webdriver.PhantomJS()

# headers = {
#     'Cookie': 'll="118316"; bid=qQH-zHRCCGA; gr_user_id=afc1b6f2-0049-42dc-81be-8d68f6cba9c0; _vwo_uuid_v2=DE721FAEDBA5FE1FC35C7EC8EEA27493F|8f41ae65b2a998a557a8db374c9354a2; viewed="3313612_2134548_2995812_1003000"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1545550586%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DyVQIEE8DOyoBSfMw5QNwtecHYe53W7tPonrLQmIGr2JDXvWPPzBoTmyq_wCj5DoH%26wd%3D%26eqid%3Dc5489949001fc66d000000065c1f3b7e%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1395709726.1544004320.1544343716.1545550588.5; __utmc=30149280; __utmz=30149280.1545550588.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; _ga=GA1.2.1395709726.1544004320; _gid=GA1.2.590144554.1545550921; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18907; __utmt=1; __yadk_uid=kXldsurDpLpirf1fIDH4SNU1Ts3TwuCS; ue="1427736474@qq.com"; dbcl2="189071734:1rmcPIyVmcw"; ck=ELeu; _pk_id.100001.8cb4=2f7fa2bbc93f0acf.1544004319.2.1545553274.1544004330.; __utmb=30149280.26.10.1545550588'
#     }
#
# url = 'https://www.douban.com/'
# # params = {
# #     'source': 'index_nav',
# #     'form_email': '1427736474@qq.com',
# #     'form_pasword': 'fei5203344'
# # }
# html = requests.get(url, headers=headers)
# print(html.text)

# html = requests.get('https://www.jianshu.com/users/898bb4ca481d/timeline/')
# etree.HTML(html.text)


# 拼接字符串
# user_id = 1
# max_id = 1
# page = 2
# next_url = 'http://www.jianshu.com.users/%s/timeline?max_id=%s&page=%s' % (user_id, max_id, page)
# print(next_url)


# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# res = requests.get('https://bj.xiaozhu.com/')  # 请求头
# soup = BeautifulSoup(res.text, 'html.parser')  # 解析数据
# 定位元素并通过selector方法提取
# prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>起/晚</span>', res.text)
# for price in prices:
#     print(price)
# print(price.get_text())  # 获取文字信息


# phone = '123-4567-1234'
# new_phone = re.findall('\d+', phone)  # re.findall()函数
# # new_phone = re.sub('\D', '', phone)  # re.sub()函数
# print(new_phone)


# a = 'one1two2three3'
# infos = re.search('\d+', a)
# print(infos)  # 返回正则表达式对象
# print(infos.group())  # group 方法返回信息


# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# res = requests.get('http://bj.xiaozhu.com/search-duanzufang-p1-0/', headers=headers)  # 请求头
# soup = BeautifulSoup(res.text, 'html.parser')  # 解析数据
# # 定位元素并通过selector方法提取
# prices = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
# for price in prices:
#     print(price.get_text())  # 获取文字信息

# requests库的使用和Beautifulsoup库的使用
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# res = requests.get('http://bj.xiaozhu.com/', headers=headers)  # get方法加入方法头
# soup = BeautifulSoup(res.text, 'html.parser')  # 对返回的结果进行解析
# print(soup.prettify())
# # soup文档的find_all方法(返回一个集合,包含所有的tag)和find方法(只返回相应的一个tag)和selector方法
# soup.find_all('div', "item")  # 查找div标签， class = "item"
# soup.find_all('div', attrs={"class": "item"})  #attrs参数定义了一个字典参数，来搜索包含特殊属性的tag
# try:
#     print(res.text)
# except ConnectionError:
#     print("拒绝连接！")

# 小猪短租网
# res = requests.get('http://bj.xiaozhu.com/')
# print(res)
# print(res.text)

