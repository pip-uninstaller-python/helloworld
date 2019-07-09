from selenium import webdriver
import csv
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)  # 连接数据库
mydb = client['mydb']  # 新建或打开数据库
qq_shuo = mydb['qq_shuo']  # 新建数据集合

driver = webdriver.PhantomJS()  # 选择浏览器
driver.maximize_window()  # 窗口最大化


def get_info(qq):
    url = 'https://user.qzone.qq.com/{}/311'.format(qq)  # 拼接链接
    driver.get(url)  # 发送请求
    driver.implicitly_wait(10)  # 隐式等待10秒
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('1427736474')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('fei5203344')
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    if b == True:
        driver.switch_to.frame('app_canvas_frame')
        contents = driver.find_elements_by_css_selector('.content')
        times = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')  # c_tx c_tx3 goDetail
        for content, tim in zip(contents, times):
            data = {
                'time': tim.text,
                'content': content.text
            }
            qq_shuo.insert_one(data)


if __name__ == '__main__':
    qq_lists = []
    fp = open('F:/QQmail.csv', encoding='utf-8')
    reader = csv.DictReader(fp)
    for row in reader:
        qq_lists.append(row['电子邮件'].split('@')[0])  # 存入qq号
    fp.close()
    for item in qq_lists:
        get_info(item)

