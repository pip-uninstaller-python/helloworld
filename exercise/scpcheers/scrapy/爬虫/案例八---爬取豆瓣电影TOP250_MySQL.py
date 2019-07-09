import requests
from lxml import etree
import re
import pymysql
import time

# 爬取信息：电影名称、导演、主演、类型、制片国家、上映时间、片长、评分
conn = pymysql.connect(host='localhost', user='root', password='.Scp123456_',
                       db='mydb', port=3306, charset='utf8')
cursor = conn.cursor()  # 连接数据库及光标

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


# 获取子页面详细信息的url
def get_movie_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    hrefs = selector.xpath('//div[@class="hd"]/a/@href')
    for href in hrefs:
        get_movie_info(href)


def get_movie_info(href):
    res = requests.get(href)
    selector = etree.HTML(res.text)  # 解析html文件
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        # actor = selector.xpath('//*[@id="info"]/span[3]/span[.*?]/text()')
        actors = re.findall('<a href=".*?" rel="v:starring">(.*?)</a>', res.text, re.S)
        # 数据清洗
        i = 0
        actors_new = ''
        for actor in actors:
            if i == len(actors)-1:
                actors_new = actors_new + str(actor)
                i += 1
            else:
                actors_new = actors_new + str(actor) + '/'
                i += 1
        styles = re.findall('<span property="v:genre">(.*?)</span>', res.text, re.S)
        # 数据清洗
        i = 0
        styles_new = ''
        for style in styles:
            if i == len(styles) - 1:
                styles_new = styles_new + str(style)
                i += 1
            else:
                styles_new = styles_new + str(style) + '/'
                i += 1
        country = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>',
                            res.text, re.S)[0]
        times = re.findall(' <span property="v:initialReleaseDate" content=".*?">(.*?)</span>',
                           res.text, re.S)
        # 数据清洗
        i = 0
        times_new = ''
        for time0 in times:
            if i == len(times) - 1:
                times_new = times_new + str(time0)
                i += 1
            else:
                times_new = times_new + str(time0) + '/'
                i += 1

        runtime1 = re.findall('片长:</span>.*?>(.*?)</span>(.*?)<br/>', res.text, re.S)[0]
        runtime2 = re.findall('片长:</span>.*?</span>(.*?)<br/>', res.text, re.S)
        if len(runtime2) != 0:
            runtime = runtime1[0] + runtime2[0]
        else:
            runtime = runtime1[0]
        # score = re.findall('<strong class="ll rating_num" property="v:average">(.*?)</strong>',
        #                    res.text, re.S)[0]
        score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        print(name, director, styles_new, country, times_new, runtime, score)
        cursor.execute('insert into doubanmovie (name, director, actor, style, country, '
                       'release_time, time, score)'
                       ' values(%s,%s,%s,%s,%s,%s,%s,%s)',
                       (name, director, actors_new, styles_new,
                        country, times_new, runtime, score))
    except IndexError:  # 有些电影的链接不存在的情况
        pass


if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start={}'.format(str(i))
            for i in range(0, 50, 25)]
    for url in urls:
        get_movie_url(url)
        time.sleep(2)
    conn.commit()
