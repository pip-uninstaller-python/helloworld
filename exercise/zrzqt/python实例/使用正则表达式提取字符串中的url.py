#给定一个字符串，里面包含url,需要我们使用正则表达式来获取字符串的url.
import re
def Find(string):
    #findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',string)
    return url
string = 'zrzqt的网页地址为：https://www.github.com/zrzqt. Google的网页地址为:https://www.google.com'
print('Urls:',Find(string))
