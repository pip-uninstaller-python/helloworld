import requests
from lxml import etree
import xlwt  # 用于操作excel
import time

# /html/body/div[2]/div[5]/div[2]/div[2]/div/ul/li[1]/div[2]/h4/a

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头

all_info_list = []  # 初始化列表，用于存储信息


def get_info(url):
    html = requests.get(url, headers=headers)  # 获取页面
    selectors = etree.HTML(html.text)  # 解析html
    infos = selectors.xpath('//div[@class="book-mid-info"]')  # 定义父标签
    for info in infos:
        name = info.xpath('h4/a/text()')[0]
        autor = info.xpath('p[1]/a[1]/text()')[0]
        style1 = info.xpath('p[1]/a[2]/text()')[0]
        style2 = info.xpath('p[1]/i/text()')[0]
        style3 = info.xpath('p[1]/a[3]/text()')[0]
        style = style1 + style2 + style3
        complete = info.xpath('p[1]/span/text()')[0]
        introduce = info.xpath('p[2]/text()')[0].strip()
        info_list = [name, autor, style, complete, introduce]
        all_info_list.append(info_list)  # 数据存入列表
    time.sleep(1)  # 睡眠1秒


if __name__ == '__main__':
    urls = ['https://www.qidian.com/all?page={}'.format(str(i))
            for i in range(1, 3)]  # 构造urls
    for url in urls:
        get_info(url)

    header = ['title', 'autor', 'style', 'complete', 'introduce']  # 定义表头
    book = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    sheet = book.add_sheet('sheet1')  # 创建工作表
    for h in range(len(header)):
        sheet.write(0, h, header[h])  # 写入表头
    i = 1
    for list0 in all_info_list:
        j = 0
        for data in list0:
            sheet.write(i, j, data)
            j += 1
        i += 1  # 写入爬虫数据
    book.save('qidianxiaoshuo.xls')

    # word = info.xpath('p[3]/span/text()')[0].strip('万字')

    # print(name, autor, style, complete, introduce)

