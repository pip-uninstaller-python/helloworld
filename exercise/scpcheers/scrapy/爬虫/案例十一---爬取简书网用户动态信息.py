import requests
from lxml import etree
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']  # 打开数据库
timeline = mydb['timeline']  # 打开数据集合

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


def get_time_info(url, page):
    user_id = url.split('/')
    user_id = user_id[4]
    if url.find('page='):
        page += 1
    html = requests.get(url, headers=headers)  # 发送请求到页面
    time.sleep(1)
    selector = etree.HTML(html.text)  # 解析页面
    infos = selector.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        dd = info.xpath('div/div[1]/div/span/@data-datetime')[0]
        type = info.xpath('div/div/div/span/@data-type')[0]
        # //*[@id="feed-394992106"]/div/div/div/span
        timeline.insert_one({
            'date': dd,
            'type': type
        })
        print(dd, type)
    id_infos = selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(infos) > 1:
        feed_id = id_infos[-1]
        max_id = feed_id.split('-')[1]
        next_url = 'http://www.jianshu.com/users/%s/' \
                   'timeline?max_id=%s&page=%s' % (user_id, max_id, page)
        get_time_info(next_url, page)


if __name__ == '__main__':
    url = 'https://www.jianshu.com/users/898bb4ca481d/timeline/'
    get_time_info(url, 1)
