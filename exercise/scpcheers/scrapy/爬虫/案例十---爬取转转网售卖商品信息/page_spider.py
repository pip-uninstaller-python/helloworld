# 爬虫单位时间内请求数多，对己方机器、对方服务器都会形成压力，如果每个请求都开启一个新连接，更是如此；
# 如果服务器支持keep-alive，爬虫就可以通过多个请求共用一个连接实现“减员增效”：
# 单位时间内新建、关闭的连接的数目少了，但可实现的有效请求多了，并且也能有效降低给目标服务器造成的压力。
# urllib3、httplib2、requets支持，urllib2不支持
import requests
from lxml import etree
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Connection': 'keep-alive'
}  # 定义请求头


def get_info_from(urls):
    for url in urls:
        # url = str(url).replace('//', '')
        if url.startswith('//'):
            url = url[2:]
        else:
            pass
        if url.startswith(' '):
            url = url[1:]
        if url.startswith('http'):
            pass
        else:
            url = 'http://' + url
        res = requests.get(url, headers=headers)  # 发送请求
        time.sleep(1)
        selector = etree.HTML(res.text)  # 解析页面
        try:
            if selector.xpath('//div[@class="detail-title"]/h1/text()'):
                title = selector.xpath('//div[@class="detail-title"]/h1/text()')[0].strip()
            else:
                title = '无'
            if selector.xpath('//div[@class="detail-title"]/div[1]/div[1]/text()'):
                publishtime = selector.xpath('//div[@class="detail-title"]/div[1]/div[1]/text()')[0].strip()
            else:
                publishtime = '无'
            if selector.xpath('//div[@class="detail-title"]/div/div/span/text()'):
                span = selector.xpath('//div[@class="detail-title"]/div/div/span/text()')[0].strip()
            else:
                span = '无'
            if selector.xpath('//div[@class="infocard__container haveswitch"]/div[1]/div[2]/span/text()'):
                price = selector.xpath('//div[@class="infocard__container haveswitch"]/div[1]/div[2]/span/text()')[0].\
                    strip()
            else:
                price = '无'
            if selector.xpath('//div[@class="infocard__container haveswitch"]/div[2]/div[2]/text()'):
                quality = selector.xpath('//div[@class="infocard__container haveswitch"]/div[2]/div[2]/text()')[0].\
                    strip()
            else:
                quality = '无'
            if selector.xpath('//div[@class="infocard__container haveswitch"]/div[3]/div[2]/a/text()'):
                addresses = selector.xpath('//div[@class="infocard__container haveswitch"]/div[3]/div[2]/a/text()')
                address = ''
                for address0 in addresses:
                    address += address0
            else:
                address = '无'
            info = {
                '标题': title,
                '发布时间': publishtime,
                '浏览次数': span,
                '价格': price,
                '成色': quality,
                '地点': address,
                'URL': url
            }
            print(info)
            return
        except IndexError:
            pass

    '''
    //*[@id="basicinfo"]/div[3]/div[1]/div[2]/span
    
    //*[@id="basicinfo"]/div[3]/div[1]/div[2]/span
    //*[@id="basicinfo"]/div[3]/div[2]/div[2]
    //*[@id="basicinfo"]/div[3]/div[3]/div[2]
    
    //*[@id="basicinfo"]/div[2]/div[1]/div[2]
    //*[@id="basicinfo"]/div[2]/div[2]/div[2]
    //*[@id="basicinfo"]/div[2]/div[3]/div[2]
    '''

