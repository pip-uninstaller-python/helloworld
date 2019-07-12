import  datetime
import threading
import requests
import re
import queue
from lxml import etree
def dateRange(beginDate, endDate):#创建一个时间列表
    dates = queue.Queue()
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.put(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates
class mainthread(threading.Thread):
    def __init__(self,url_queue=None,name='  '):
        super().__init__()
        self.name=name
        self.url_queue=url_queue
        self.headers={'USER_AGENT ': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    def get_main(self):
        print(self.name)
        while not self.url_queue.empty():
            try:
                url=self.url_queue.get(block=False)
                res=requests.get(url,headers=self.headers)
                res.encoding = 'gb18030'
                dat=re.search(">(\d{4}年\d{2}月\d{2}日 (.*?))<",res.text)[1]
                html = etree.HTML(res.text)
                data_list = html.xpath('//tbody[1]/tr')
                lsts = [('赛事', '轮次', '比赛时间', '状态', '主队', '比分', '客队', '半场','竞彩官方','威廉希尔','澳门','Bet365','立博')]
                for i in data_list:
                    try:
                        saishi=i.xpath('./td[1]/a/text()')[0]
                        lunci=i.xpath('./td[2]/text()')[0]
                        time=i.xpath('./td[3]/text()')[0]
                        mainteam=i.xpath('./td[5]/a//text()')[0]
                        bifen = i.xpath('./td[6]/a/text()')
                        bifen=f'{bifen[0]}{bifen[1]}{bifen[2]}'
                        banc=i.xpath('./td[8]//text()')
                        cuteam=i.xpath('./td[7]//text()')[0]
                        id=i.xpath('./@id')[0]
                        id=id.strip('a')
                        self.get_ou(id)
                        tup = (saishi,lunci,time,mainteam,bifen,cuteam,banc)
                        print(tup)
                    except:
                        continue

            except:
                pass
    def get_ou(self,id):
        url=f'http://odds.500.com/fenxi/ouzhi-{id}.shtml'
        res=requests.get(url,headers=self.headers)
        res.encoding='gb18030'
        html=etree.HTML(res.text)
        try:
            data_list=html.xpath('//td[@title="竞彩官方"]/../td[3]//tr/td/text()')
        except:
            pass

        # res=etree.HTML(res.text)
if __name__=='__main__':
    list=dateRange('2016-01-01','2016-01-31')
    a=mainthread(name='1',url_queue=list)
    a.get_main()