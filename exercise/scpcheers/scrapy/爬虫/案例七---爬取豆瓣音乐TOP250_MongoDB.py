import requests
import re
import pymongo
from lxml import etree
import time

# 爬取歌曲名、表演者、流派、发行时间、出版者、评分
# 连接数据库，新建或打开数据库和数据集合
client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']  # 新建活打开mydb数据库
musictop = mydb['musictop']  # 创建数据集合

# 定义浏览器访问头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


# 传入主页面，获取详细信息的url
def get_url_music(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//tr[@class="item"]/td/div/a/@href')
    for music_href in music_hrefs:
        get_music_info(music_href)


# 获取音乐的详细信息
def get_music_info(music_href):
    html = requests.get(music_href, headers=headers)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    autor = re.findall('表演者:.*?>(.*?)</a>',
                       html.text, re.S)[0]
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',
                        html.text, re.S)
    if len(styles) == 0:
        style = '未知'
    else:
        style = styles[0].strip()
    # 利用xpath语法提取数据会比较乱，多个标签相互嵌套，还有一些乱码的符号，给数据清理带来很多麻烦
    time0 = re.findall('<span class="pl">发行时间:</span>&nbsp;(.*?)<br />',
                      html.text, re.S)[0].strip()
    score = re.findall('<strong class="ll rating_num" property="v:average">(.*?)</strong>',
                       html.text, re.S)[0]
    publisher = re.findall('<span class="pl">出版者:</span>&nbsp;(.*?)<br />',
                           html.text, re.S)[0].strip()
    print(name, autor, style, time0, score, publisher)
    info = {
        '歌曲名': name,
        '表演者': autor,
        '流派': style,
        '发行时间': time0,
        '出版者': publisher,
        '豆瓣评分': score
    }
    musictop.insert_one(info)  # 插入数据


if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i))
            for i in range(0, 50, 25)]
    for url in urls:
        get_url_music(url)
        time.sleep(2)

