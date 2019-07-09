import requests
from lxml import etree
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}   # 加入请求头

urls = ['http://zs.henau.edu.cn/zhuanyejieshao/20170518/{}.html'.format(str(i))
        for i in range(117, 135)]  # 构造urls

for url in urls:
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)  # 解析HTML文件
    print(res.text)
    try:
      url_infos = selector.xpath('//div[@class="content"]/text()')[0]
      print(url_infos)
      time.sleep(1)  # 暂停1s
    except IndexError:
      pass

