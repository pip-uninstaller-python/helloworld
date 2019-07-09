from selenium import webdriver

url = 'https://www.jianshu.com/p/c71aafad3524'


def get_info(url):
    include_title = []  # 初始化列表，存入收录专题的信息
    driver = webdriver.PhantomJS()  # 选择浏览器
    driver.get(url)  # 发送请求
    driver.implicitly_wait(20)  # 隐式等待20秒
    autor = driver.find_element_by_xpath('//span[@class="name"]/a').text
    date = driver.find_element_by_xpath('//span[@class="publish-time"]').text
    word = driver.find_element_by_xpath('//span[@class="wordage"]').text
    view = driver.find_element_by_xpath('//span[@class="views-count"]').text
    comment = driver.find_element_by_xpath('//span[@class="comments-count"]').text
    like = driver.find_element_by_xpath('//span[@class="likes-count"]').text
    included_names = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
    for i in included_names:
        include_title.append(i.text)
    print(autor, date, word, view, comment, like, include_title)


get_info(url)

