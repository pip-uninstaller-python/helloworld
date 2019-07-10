import requests
import re
from lxml import etree
import csv
import pandas as pd
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
def get_link(url):
    res=requests.get(url,headers=headers)
    res=etree.HTML(res.text)
    url_list=res.xpath('//div[@id="page_list"]/ul/li/a/@href')
    return url_list
def get_detail(url):
    res=requests.get(url,headers=headers)
    res=etree.HTML(res.text)
    title=res.xpath('//h4[1]/em/text()')[0]
    address=res.xpath('//span[@class="pr5"]/text()')[0]
    address=address.strip()
    price=res.xpath('//div[@id="pricePart"]/div/span/text()')[0]
    tiaoj=res.xpath('//div[@class=" intro_item_content"]/p/text()')
    a=''
    for i in tiaoj:
        i = re.sub('\s', '', i)
        a+=i
    tiaoj=a

    data={
        'name':title,
        'address':address,
        'price':price,
        '条件':tiaoj
    }
 #   print(data)
    save_csv(data)
def save_csv(data):
    # dataf=pd.DataFrame(data)
    # dataf.to_csv('aa.csv',index=False,sep=',',mode='a')
    da=[data['name'],data['address'],data['price'],data['condition']]
    with open('aa.csv','a',newline='',encoding='utf-8') as f:
        a=csv.writer(f)
        a.writerow(da)

if __name__=='__main__':
    type=input('请输入你要找的房间类型： 整套出租/独立单间/合住房间')
    dict={'整套出租':'zhengzu','独立单间':'danjian','合住房间':'shafa'}
    kw=dict[type]
    #print(dict[type])
    a=int(input('请输入要爬取多少页数据：'))
    with open('aa.csv','w',newline='')as f:
        file=csv.writer(f)
        list=['name','address','price','条件']
        file.writerow(list)
    for i in range(1,a+1):
        url=f'http://hf.xiaozhu.com/{kw}-duanzufang-p{i}-2/'
        url_list=get_link(url)
        for xurl in url_list:
            get_detail(xurl)
    print('完成爬取')