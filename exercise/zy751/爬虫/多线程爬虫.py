import requests
import threading
import queue
from lxml import etree
import json
def get_url():
    url_queue=queue.Queue()
    for i in range(0,250,25):
        url=f'https://movie.douban.com/top250?start={i}&filter='
        url_queue.put(url)
    return url_queue
class paqu(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        while not url_queue.empty():
            try:
                url=url_queue.get(block=False)
                print(f'爬取线程{self.name}')
                response=requests.get(url,headers=headers).text
                response_queue.put(response)
            except:
                pass

class jiexi(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        while flag:
            try:
                text=response_queue.get(block=False)
                print(f'解析线程{self.name}')
                text=etree.HTML(text)
                data=self.parse(text)
                for dat in data:
                    a.write(json.dumps(dat,ensure_ascii=False)+'\n')
            except:
                pass
    def parse(self,text):
        try:
            info_list=text.xpath('//div[@class="info"]')
            for info in info_list:
                url=info.xpath('./div/a/@href')[0]
                name=info.xpath('./div/a/span[1]/text()')[0]
                print(url,name)
                yield url,name
        except:
            pass
if __name__=='__main__':
    print('主线程开始')
    a=open('电子.txt','a',encoding='utf-8')
    url_queue=get_url()
    response_queue=queue.Queue()
    flag=True
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    list1=[]
    list2=[]
    for i in range(3):
        obj=paqu(i)
        obj.start()
        list1.append(obj)
    for j in range(4):
        obj=jiexi(j)
        obj.start()
        list2.append(obj)
    while not url_queue.empty():
        pass
    for i in list1:
        i.join()
    while not response_queue.empty():
        pass
    flag=False
    for j in list2:
        j.join()
    a.close()
    print('主线程结束')


