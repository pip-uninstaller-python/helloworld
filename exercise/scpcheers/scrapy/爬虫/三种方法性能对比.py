import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time  # 用于计时

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}   # 加入请求头

urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i))
        for i in range(1, 36)]  # 构造urls


def re_scraper(url):  # 使用正则爬虫
    res = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)'
                        '</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i>', res.text, re.S)
    for id, content, laugh, comment in zip(
        ids, contents, laughs, comments):
        info = {
            'id': id,
            'content': content,
            'laugh': laugh,
            'comment': comment
        }
        return info  # 只返回数据，不存储


def bs_scraper(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    ids = soup.select('a > h2')
    contents = soup.select('div > span')
    laughs = soup.select('span.stats-vote > i')
    comments = soup.select('i.number')
    for id, content, laugh, comment in zip(
            ids, contents, laughs, comments):
        info = {
            'id': id.get_text().strip(),
            'content': content.get_text().strip(),
            'laugh': laugh.get_text(),
            'comment': comment.get_text()
        }
        return info  # 只返回数据，不存储


def lxml_scraper(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)  # 解析HTML文件
    url_infos = selector.xpath('//div[@class="article block untagged mb15 typs_hot"]')
    url_infoss = selector.xpath('//div[@class="article block untagged mb15 typs_long"]')
    url_infosss = selector.xpath('//div[@class="article block untagged mb15 typs_old"]')
    url_infos.extend(url_infoss)
    url_infos.extend(url_infosss)
    try:
        for url_info in url_infos:
            id = url_info.xpath('div[1]/a[2]/h2/text()')[0]
            content = url_info.xpath('a[1]/div/span[1]/text()')[0]
            laugh = url_info.xpath('div[2]/span[1]/i/text()')[0]
            comment = url_info.xpath('div[2]/span[2]/a/i/text()')[0]
            info = {
                'id': id,
                'content': content,
                'laugh': laugh,
                'comment': comment
            }
            return info
    except IndexError:
        pass


if __name__ == '__main__':
    # for url in urls:
    #     re_scraper(url)
    for name, scraper in [('Regularexpressions', re_scraper),
                          ('BeautifulSoup', bs_scraper),
                          ('Lxml', lxml_scraper)]:
        start = time.time()  # 开始计时
        for url in urls:
            scraper(url)
        end = time.time()  # 结束计时
        print(name, end-start)  # 结束时间减去开始时间

