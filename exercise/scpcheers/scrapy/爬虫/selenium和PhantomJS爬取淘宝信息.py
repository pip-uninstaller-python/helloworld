from selenium import webdriver
from lxml import etree
import time
import pymongo
# https://uland.taobao.com/sem/tbsearch?spm=a2e15.8261149.07626516003.3.45d729b4hInFyG&refpid=mm_26632258_3504122_3253
# 8762&clk1=31dd250d66b241d7c665d64d3ffaa134&keyword=%E7%9F%AD%E8%A2%96t%E6%81%A4%20%E7%
# 94%B7&page=1&_input_charset=utf-8

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']  # 打开数据库
taobao = mydb['taobao']  # 新建数据集合

driver = webdriver.PhantomJS()  # 选择浏览器
driver.maximize_window()  # 窗口最大化


def get_info(url, page):
    page = page + 1
    driver.get(url)  # 发送请求
    driver.implicitly_wait(10)  # 隐式等待10秒
    selector = etree.HTML(driver.page_source)  # 请求网页源代码
    infos = selector.xpath('//div[@class="info"]')  # 获取每个小页面的头
    for info in infos:
        price = info.xpath('p[1]/span[1]/strong/text()')
        # //*[@id="ItemWrapper"]/div[1]/a/div[2]/p[1]/span[1]/strong
        print(price)

    if page <= 2:
        NextPage(url, page)
    else:
        pass


def NextPage(url, page):
    driver.get(url)
    driver.implicitly_wait(10)  # 隐式等待十秒
    driver.find_element_by_xpath('//a[@class="page-next iconfont"]').click()
    time.sleep(4)
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    get_info(driver.current_url, page)  # 获取当前页面的url


if __name__ == '__main__':
    page = 1
    url = 'https://uland.taobao.com/sem/tbsearch?page=1&_input_charset=utf-8'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()  # 清空输入框
    driver.find_element_by_id('q').send_keys('男士短袖')  # 输入要搜索的值
    driver.find_element_by_class_name('submit').click()
    get_info(driver.current_url, page)

