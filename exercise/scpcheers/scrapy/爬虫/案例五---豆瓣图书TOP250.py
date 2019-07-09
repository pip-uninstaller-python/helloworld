import requests  # 获取html
from lxml import etree  # 解析html
import csv  # 存储为csv文件
import time  # 计时


fp = open('F:/douban.csv', 'wt', newline='',
          encoding='utf-8')  # 创建csv文件，newline:换行设置，wt:mode设置，默认为rt
writer = csv.writer(fp)
writer.writerow(('name', 'url', 'autor', 'publisher', 'date',
                 'price', 'rate', 'comment'))  # 写入header

urls = ['https://book.douban.com/top250?start={}'.format(str(str(i)))
        for i in range(0, 250, 25)]  # 构造urls

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}   # 加入请求头

start = time.time()
for url in urls:
    html = requests.get(url, headers=headers)  # 通过requests获取文件
    selector = etree.HTML(html.text)  # 通过lxml库解析文件
    infos = selector.xpath('//tr[@class="item"]')  # 取大标签
    for info in infos:
        name = info.xpath('td[2]/div[1]/a/@title')[0]
        url = info.xpath('td[1]/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        autor = book_infos.split('/')[0]
        book_publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td[2]/div[2]/span[2]/text()')[0]
        comments = info.xpath('td[2]/p[2]/span/text()')
        if len(comments) == 0:
            comment = '评论为空'
        else:
            comment = comments[0]
        writer.writerow((name, url, autor, book_publisher, date, price, rate, comment))
fp.close()
end = time.time()
print('用时：' + str(end-start))


# fp = open("F:/test.csv", 'w+')  # 创建csv文件
# writer = csv.writer(fp)
# writer.writerow(('id', 'name'))
# writer.writerow(('1', '小明'))
# writer.writerow(('2', '张三'))
# writer.writerow(('3', '李四'))

