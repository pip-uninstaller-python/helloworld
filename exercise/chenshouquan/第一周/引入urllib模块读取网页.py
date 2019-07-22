import urllib.request #引入urllib模块

#from urllib import request #from引入模块方法

url=r"http://www.baidu.com"#加转义字符r防止有转义字符

#发送请求.获取响应信息
reponse=request.urlopen(url).read()

print(reponse)#打印出读取内容（二进制）
print(len(reponse))#打印一下显示有多少长度


'''#下面用from引入模块写法
from urllib import request #引入模块方法

url=r"http://www.baidu.com"#加转义字符r防止有转义字符

#发送请求.获取响应信息
reponse=request.urlopen(url).read()#from引入的模块前缀urllib全部不用写

print(reponse)#打印出读取内容（二进制）
print(len(reponse))#打印一下显示有多少长度'''