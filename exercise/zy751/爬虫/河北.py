import re
import time
import csv
import requests
def get_list(num):
    data={
        'start':num,
        'limit':'20',
        'type':'1',
    }
    res=requests.post(url,data=data,verify=False).text
    id=re.findall(r'"id":(\d+)',res)
    return id
def get_detail(id):
    data={
        'id': id
    }
    res=requests.post(post_url,data=data,verify=False).text
    title=re.search(r'"title":"(.*?)"',res)[1]
    print(title)
    hit = re.search(r'"hit":(\d+)',res)[1]
    print(hit)
    da= re.search(r'"createDate":(\d+)',res)[1]
    ctime=time.localtime(int(int(da)//1000))#采集的为时间戳，切X1000了要还原 再解析
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", ctime)
    print(otherStyleTime)
    content=re.search(r'"content":"(.*?)",',res)[1]
    content=re.sub(r'<p style=\\"text-indent:2em;\\">|\\r|\\n|\\t|</p>|<p align=(.*?)>|<img alt=(.*?)>','',content)
    print(content)
    item=[title,hit,data,content]
    return item

def save_csv(item):
    with open('aa.csv','a',encoding='utf-8') as f:
        a=csv.writer(f)
        a.writerow(item)
if __name__=='__main__':
    url="https://www.hbfu.edu.cn/news/queryListForPage"
    post_url='https://www.hbfu.edu.cn/news/findById'
    ids=get_list(0)
    for i in ids:
        a=get_detail(i)
        save_csv(a)
