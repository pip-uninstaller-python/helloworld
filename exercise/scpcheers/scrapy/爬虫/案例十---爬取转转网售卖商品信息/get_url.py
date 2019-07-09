import requests
from lxml import etree
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Connection': 'keep-alive'
}  # 定义请求头

start_url = 'https://haikou.58.com/sale.shtml'  # 主页面url
url_host = 'https://haikou.58.com'  # 拼接的主页面url头


def get_class_urls(url):  # 获取分类的url
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="ym-submnu"]/li/b/a/@href')
    class_urls0 = []  # 存储到列表中，存在重复数据
    for info in infos:
        # print(url_host + info)
        class_urls0.append(url_host + info)
    class_urls = list(set(class_urls0))  # 数据清洗（通过转为集合再转为列表的形式消除重复数据）
    return class_urls
    # i = len(class_urls2)
    # print(i)  # 分类页面存在58条url，即58个分类


def get_class_detail_url(class_url, i):  # 获取分类页面打开的页面
    list_view = class_url + 'pn{}/'.format(str(i))
    try:
        res = requests.get(list_view, headers=headers)  # 发送请求
        time.sleep(1)
        selector = etree.HTML(res.text)  # 解析页面
        if selector.xpath('//td[@class="img"]/a/@href'):
            good_links = selector.xpath('//td[@class="img"]/a/@href')  # 获取商品信息页面链接
            # for good_link in good_links:
            #     print(good_link)
            return good_links
        else:
            pass
    except requests.exceptions.ConnectionError:
        pass  # pass掉请求连接错误

