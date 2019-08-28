from execjs import compile
from time import time,sleep
from requests import post
def get_js():
    f=open('F:\JS\网易云js.js','r',encoding='utf8')
    line=f.readline()
    content=''
    while line:
        content=content+line
        line=f.readline()
    return content
jsstr=get_js()
ctx=compile(jsstr)
sign=ctx.call('sign','苹果')
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
str1=input('请你输入你要翻译的内容')
data={'i': str1,
      'from': 'AUTO',
      'to': 'AUTO',
      'smartresult': 'dict',
      'client': 'fanyideskweb',
      'salt': str(int(time()*10000)),
     'sign': sign,
      'ts': str(int(time()*1000)),
      'bv': 'f0325f69e46de1422e85dedc4bd3c11f',
      'doctype': 'json',
      'version': '2.1',
      'keyfrom': 'fanyi.web',
      'action': 'FY_BY_CLICKBUTTION'}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer':'http://fanyi.youdao.com/?keyfrom=fanyi.logo'
}
response=post(url,data=data,headers=headers).json()
print(response['translateResult'][0][0]['tgt'])
sleep(10)