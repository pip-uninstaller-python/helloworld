# 多进程爬虫
import requests
from lxml import etree
import re
from multiprocessing import Pool
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']  # 打开数据库
jianshou_daketang = mydb['jinshu_daketang']  # 打开或新建数据集合

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


def get_info(url):
    try:
        html = requests.get(url, headers=headers)  # 请求网页
        selector = etree.HTML(html.text)  # 解析爬取网页数据
        ids = selector.xpath('//a[@class="title"]/text()')
        contents = selector.xpath('//p[@class="abstract"]/text()')
        comments = re.findall('<i class="iconfont ic-list-comments"></i>(.*?)</a>',
                              html.text, re.S)
        # comments = selector.xpath('//a[@target="_blank"]/text()')
        likes = re.findall('<span><i class="iconfont ic-list-like"></i>(.*?)</span>',
                           html.text, re.S)
        moneys = re.findall('<span><i class="iconfont ic-list-money"></i>(.*?)</span>',
                            html.text, re.S)
        for id, content, comment, like, money in zip(ids, contents, comments, likes, moneys):
            info = {
                'id': id,
                'content': content,
                'like': like,
                'money': money
            }
            jianshou_daketang.insert_one(info)
    except IndexError:
        pass


if __name__ == '__main__':
    urls = ['https://www.jianshu.com/c/e048f1a72e3d?order_by=added_at&page={}'.format
            (str(i)) for i in range(2, 15)]
    # start_time = time.time()
    # for url in urls:
    #     get_info(url)
    # end_time = time.time()
    # print('串行爬虫用时：' + str(end_time-start_time))
    start_time = time.time()
    pool = Pool(processes=2)
    pool.map(get_info, urls)
    end_time = time.time()
    print('双进程爬虫用时：' + str(end_time - start_time))

