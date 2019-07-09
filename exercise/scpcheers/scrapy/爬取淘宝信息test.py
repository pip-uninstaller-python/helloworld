import requests
from lxml import etree
from multiprocessing import Pool

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


def get_info(url):
    html = requests.get(url, headers=headers)  # 发送请求
    selector = etree.HTML(html.text)  # 解析页面
    money = selector.xpath('//div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]/div[1]/div[1]/strong/text()')
    print(money)
    # infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')  # 获取xpath头
    # for info in infos:
    #     money = info.xpath('div[2]/div[1]/div[1]/strong/text()')[0]
    #     print(money)


if __name__ == '__main__':
    url = 'https://s.taobao.com/list?q=%E5%81%A5%E8%BA%AB%E5%99%A8&cat=50010728'
    get_info(url)

