import requests
from lxml import etree
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


def get_info(url):
    html = requests.get(url, headers=headers)
    time.sleep(1)
    selector = etree.HTML(html.text)  # 解析html文件
    # 获取大标签 --- li
    infos_head = selector.xpath('//*[@id="shop-all-list"]/ul/li')
    for head in infos_head:
        name = head.xpath('div[2]/div[1]/a[1]/h4/text()')[0]
        dianping = head.xpath('div[2]/div[2]/a[1]/b/svgmtsi[1]/text()')
        print(dianping)


if __name__ == '__main__':
    urls = ['http://www.dianping.com/shanghai/ch10/g215p{}'.format(str(i))
            for i in range(1, 5)]
    for url in urls:
        get_info(url)


