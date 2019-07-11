import requests
import re
import csv
from lxml import etree
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# ipurl = 'http://127.0.0.1:5010/get/'
# r = requests.get(ipurl)
# proxy = {#设置proxies
#     'http': f'{r.text}',
#     'https': f'{r.text}'
# }
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
def get_href(url):#获取当前页面电影网址
    res = requests.get(url,headers=headers).text
    res=etree.HTML(res)
    herf=res.xpath("//ol/li//div[@class='hd']/a/@href")
    return herf
def get_detail(url):#获取详情页内容
    res=requests.get(url,headers=headers).text
    res = etree.HTML(res)
    name=res.xpath('//head/title/text()')[0]
    name=name.strip()
    png=res.xpath('//div[@id="mainpic"]/a/img/@src ')[0]
    score=res.xpath('//strong[@property="v:average"]/text()')[0]
    ratingcount=res.xpath('//span[@property="v:votes"]/text()')[0]
    content=res.xpath('//span[@property="v:summary"]/text()')[0]
    content=content.strip()
    item=[name,png,score,ratingcount,content]
    return item
def save_svc(data):
    with open("bb.csv",'a',encoding='utf-8')as f:
        b=csv.writer(f)
        b.writerow(data)
if __name__=='__main__':
    for i in range(0,25,25):#可实现翻页
        url = f"https://movie.douban.com/top250?start={i}&filter="
        a=get_href(url)
        for j in a:
            data=get_detail(j)
            print(data)
            save_svc(data)