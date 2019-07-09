from selenium import webdriver

# 实现豆瓣登陆，获取网页代码
driver = webdriver.PhantomJS()  # 指定浏览器
driver.maximize_window()  # 窗口最大化
driver.get('https://www.douban.com/')  # 请求url
# 隐式等待的优点：解释完JavaScript立刻进行下一步
# time.sleep的缺点：强制停止一个固定时间，时间短了，则没法解释完JavaScript，可能导致无法正常获取数据
driver.implicitly_wait(10)  # 隐式等待十秒
driver.find_element_by_id('form_email').clear()  # 清除输入框数据
driver.find_element_by_id('form_email').send_keys('13137761670')  # 输入账号
driver.find_element_by_id('form_password').clear()  # 清除密码输入框数据
driver.find_element_by_id('form_password').send_keys('fei5203344')  # 输入密码
driver.find_element_by_class_name('bn-submit').click()  # 单击登入框
print(driver.page_source)
