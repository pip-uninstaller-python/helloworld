import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}   # 加入请求头


def judgement_sex(class_name):
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'


def get_links(url):  # 定义获取详细页url的函数
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#page_list > ul > li > a')  # links为url列表
    for link in links:
        href = link.get("href")
        get_info(href)  # 循环出的url，依次调用get_info函数


def get_info(url):  # 定义获取网页信息的函数
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    tittles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for tittle, address, price, img, name, sex in zip(
            tittles, addresses, prices, imgs, names, sexs):
        data = {
            '标题': tittle.get_text().strip(),
            '地点': address.get_text().strip(),
            '日租价格': price.get_text(),
            '图片链接': img.get("src"),
            '租客名': name.get_text(),
            '性别': judgement_sex(sex.get("class"))
        }
        print(data)  # 获取信息通过字典的信息打印


if __name__ == '__main__':  # 程序的主入口
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number)
            for number in range(1, 5)]  # 构造多页url
    print(urls)
    for single_url in urls:
        get_links(single_url)  # 循环调用get_link()函数
        time.sleep(3)  # 睡眠两秒


