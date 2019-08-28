from selenium import webdriver
#导入相关模块
######################################################
#正常模式

Browser = webdriver.Chrome()
#打开浏览器
Browser.get('http://www.baidu.com')
#访问百度首页
Browser.find_element_by_id('kw').send_keys('新笔趣阁')
#找到百度首页的搜索框并输入新笔趣阁，此处可以输入汉字
Browser.find_element_by_id('su').click()
#通过命令找到百度一下按键并点击

#########################################################
#无头模式

from selenium.webdriver.chrome.options import Options
#导入相关模块
chrome_options = Options()
#定义options变量
chrome_options.add_argument('--headless')
#定义options变量的模式
Browser = webdriver.Chrome(options = chrome_options)
#打开浏览器（未无头模式，即浏览器不显示）

###########################################################
