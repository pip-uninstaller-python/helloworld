import requests
from lxml import etree
import re
import time
import json
import pymongo
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
sevenday = mydb['sevenday']

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


def get_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('ul[@class="note-list"]/li')
    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        get_info(article_url_part)


def get_info(url):
    article_url = 'http://www.jianshu.com/' + url
    html = requests.get(article_url)
    selector = etree.HTML(html.text)
    id = re.findall('{"id":(.*?),', html.text, re.S)[0]
    gain_url = 'http://www.jianshu.com/notes/{}/rewards?count=20'.format(id)
    wb_data = requests.get(gain_url, headers=headers)
    json_data = json.loads(wb_data.text)
    gain = json_data['rewards_count']
    print(gain)


if __name__ == '__main__':
    urls = ['http://www.jianshu.com/trending/weekly?page={}'.format(str(i))
            for i in range(0, 11)]
    pool = Pool(processes=4)
    pool.map(get_url, urls)

