


#import urllib.request #引入urllib模块
from urllib import request #from引入模块方法 推荐！
import re #正则
import random #随机数 增加请求头随机


url=r"http://www.baidu.com"#加转义字符r防止有转义字符

agent1="Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)"

agent2="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

agent3="Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.6.4.950 UWS/2.11.1.50 Mobile Safari/537.36 AliApp(DingTalk/4.5.8) com.alibaba.android.rimet/10380049 Channel/227200 language/zh-CN"

agent4="Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN"

agent5="Mozilla/5.0 (Linux; Android 8.1.0; ALP-AL00 Build/HUAWEIALP-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.11 (Baidu; P1 8.1.0)"

list1=[agent1,agent2,agent3,agent4,agent5]#把agent放入列表

agent=random.choice(list1)
print(agent)

#构造请求头信息
header={"User-Agent": "agent"}
#创建自定义请求对象
#反爬虫机制1：判断用户是否是浏览器访问
#可以通过伪装浏览器进行访问
req=request.Request(url,headers=header)

#发送请求.获取响应信息
reponse=request.urlopen(req).read().decode()#解码---(（编码）encode())
#reponse=urllib.request.urlopen(req).read()#引入的模块前缀urllib全部要写

pat=r"<title>(.*?)</title>"#通过正则表达式进行数据清洗
data=re.findall(pat,reponse)
print(data[0])#data是一个列表并且只有一个字符串
#print(reponse)#打印出读取内容（二进制）
#print(len(reponse))#打印一下显示有多少长度


