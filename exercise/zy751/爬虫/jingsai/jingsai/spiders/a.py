# -*- coding: utf-8 -*-
import scrapy
import csv
import datetime
import re
f=open('aa.csv','a',newline='')
file=csv.writer(f)
file.writerow(['日期','赛事','轮次','时间','主队','客队','半场','竞彩官方','返还率','威廉希尔','返还率','立博','返还率','Bet365','返还率','澳门','返还率'])
def dateRange(beginDate, endDate):#创建一个时间列表
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates
list1=dateRange('2016-01-01', '2016-01-31')#定义一个时间列表为全局变量
def chuli(str,item):
    a=','.join(item[str+'欧赔'][:3])
    b = ','.join(item[str + '欧赔'][3:])
    c=','.join(item[str+'让球欧赔'][:3])
    d= ','.join(item[str + '让球欧赔'][3:])
    e=','.join(item[str+'即时大小'])
    f=','.join(item[str+'变化时间'])
    g=','.join(item[str+'初始大小'])
    final=f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}'
    return final
list1=dateRange('2016-01-01', '2016-01-31')#定义一个时间列表为全局变量
class ASpider(scrapy.Spider):
    name = 'a'
    start_urls = ['https://live.500.com/wanchang.php?e=2016-01-01']
    def parse(self, response):#获取指定日期的首页元素
        data_list=response.xpath('//tbody[1]/tr')
        url = response.text
        for i in data_list:
            item = {'日期':'',
                    '赛事':'',
                    '轮次': '',
                    '时间': '',
                    '主队': '',
                    '客队':'',
                    '半场': '',
                    '竞彩官方欧赔': ['','','','','',''],'竞彩官方返还率': ['',''],
                    '威廉希尔欧赔': ['','','','','',''],'威廉希尔返还率': ['',''],
                    '立博欧赔':['','','','','',''],'立博返还率': ['',''],
                    'Bet365欧赔': ['','','','','',''], 'Bet365返还率': ['',''],
                    '澳门欧赔': ['','','','','',''], '澳门返还率': ['',''],
                    '竞彩官方让球': '', '竞彩官方让球欧赔': ['','','','','',''],'竞彩官方让球返还率':['',''],
                    '威廉希尔让球': '', '威廉希尔让球欧赔': ['','','','','',''], '威廉希尔让球返还率': ['',''],
                    '澳门让球': '', '澳门让球欧赔': ['','','','','',''], '澳门让球返还率': ['',''],
                    '立博让球': '', '立博让球欧赔': ['','','','','',''], '立博让球返还率': ['',''],
                    'Bet365让球': '', 'Bet365让球欧赔': ['','','','','',''], 'Bet365让球返还率': ['',''],
                    '威廉希尔即时大小': ['','',''],'威廉希尔变化时间': '','威廉希尔初始大小':['','',''],
                    '澳门即时大小': ['','',''], '澳门变化时间': '', '澳门初始大小': ['','',''],

                    '立博即时大小': ['','',''], '立博变化时间': '', '立博初始大小': ['','',''],
                    'Bet365即时大小': ['','',''], 'Bet365变化时间': '', 'Bet365初始大小': ['','',''],
                    '竞彩官方即时大小': ['','',''], '竞彩官方变化时间': ['','',''], '竞彩官方初始大小': ['','',''],
                    }
            try:
                item['日期'] = re.search(">(\d{4}年\d{2}月\d{2}日 (.*?))<", url)[1]
                item['赛事']=i.xpath('./td[1]/a/text()').extract_first()
                item['轮次']=i.xpath('./td[2]/text()').extract_first()
                item['时间']=i.xpath('./td[3]/text()').extract_first()
                item['主队'] = i.xpath('./td[5]/a//text()').extract_first()
                item['客队'] = i.xpath('./td[7]//text()').extract_first()
                item['半场'] = i.xpath('./td[8]//text()').extract_first()
                id=i.xpath('./@id').extract_first()
               # if id:
                id=id.strip('a')#找到id 方便进入详情页
                ou_url=f'http://odds.500.com/fenxi/ouzhi-{id}.shtml?ctype=2'
                yield scrapy.Request(
                    ou_url,
                    callback=self.parse_ou,
                    meta={'item':item,'id':id}
                )
            except:
                continue
        for i in list1:
            next_url = f'https://live.500.com/wanchang.php?e={i}'
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )
    def parse_ou(self,response):
        item=response.meta['item']
        id=response.meta['id']
        rang_url=f'http://odds.500.com/fenxi/rangqiu-{id}.shtml?ctype=2'
        try:
            data_list=response.xpath('//td[@title="竞彩官方"]|//td[@title="威廉希尔"]|//td[@title="澳门"]|//td[@title="立博"]|//td[@title="Bet365"]')
            for dat in data_list:
                item[dat.xpath('./@title').extract_first() + '欧赔'] = dat.xpath('../td[3]//tr/td/text()').extract()
                item[dat.xpath('./@title').extract_first() + '返还率'] = dat.xpath('../td[5]//td/text()').extract()
                yield scrapy.Request(
                    rang_url,
                    callback=self.parse_rang,
                    meta={'item':item,'id':id}
                )
        except:
            pass
    def parse_rang(self,response):
        item=response.meta['item']
        id=response.meta['id']
        da_url=f'http://odds.500.com/fenxi/daxiao-{id}.shtml?ctype=2'
        #|//td[@title="威廉希尔"]
        try:
            data_list=response.xpath('//td[@title="竞彩官方"]|//td[@title="澳门"]|//td[@title="立博"]|//td[@title="Bet365"]')
            for dat in data_list:
                if dat.xpath('../td[3]/text()').extract_first()=='-1':
                    item[dat.xpath('./@title').extract_first() + '让球'] = dat.xpath('../td[3]/text()').extract_first()
                    item[dat.xpath('./@title').extract_first() + '让球欧赔'] = dat.xpath('../td[4]//td/text()').extract()
                    item[dat.xpath('./@title').extract_first() + '让球返还率'] = dat.xpath('../td[6]//td/text()').extract()
                    yield scrapy.Request(
                        da_url,
                        callback=self.parse_da,
                        meta={'item':item,'id':id})
                else:
                    continue
        except:
            pass
    def parse_da(self,response):
        item=response.meta['item']
        #//a[@title="竞彩官方"]|
        try:
            data_list=response.xpath('//a[@title="威廉希尔"]|//a[@title="澳门"]|//a[@title="立博"]|//a[@title="Bet365"]')
            for dat in data_list:
                item[dat.xpath('./@title').extract_first() + '即时大小'] = dat.xpath('../../../td[3]//td[position()<4]/text()').extract()
                item[dat.xpath('./@title').extract_first() + '变化时间'] = dat.xpath('../../../td[4]//text()').extract_first()
                item[dat.xpath('./@title').extract_first() + '初始大小'] = dat.xpath('../../../td[5]//td/text()').extract()
        except:
            pass
        a=chuli('竞彩官方',item)
        b=chuli('威廉希尔',item)
        c=chuli('立博',item)
        d=chuli('Bet365',item)
        e=chuli('澳门',item)
        if item['竞彩官方欧赔'][0]!='':
            list_a = [item['日期'], item['赛事'], item['轮次'], item['时间'], item['主队'], item['客队'], item['半场'],
                  a, '返还率'+'\n'+item['竞彩官方返还率'][0]+'\n'+item['竞彩官方返还率'][1]+'\n'+'让球返还率'+'\n'+item['竞彩官方让球返还率'][0]+'\n'+item['竞彩官方让球返还率'][1], b,'返还率'+'\n'+ item['威廉希尔返还率'][0]+'\n'+item['威廉希尔返还率'][1]+'\n'+'让球返还率'+'\n'+item['威廉希尔让球返还率'][0]+'\n'+item['威廉希尔让球返还率'][1], c,
                  '返还率'+'\n'+item['立博返还率'][0]+'\n'+item['立博返还率'][1]+'\n'+'让球返还率'+'\n'+item['立博让球返还率'][0]+'\n'+item['立博让球返还率'][1], d,'返还率'+'\n'+ item['Bet365返还率'][0]+'\n'+item['Bet365返还率'][1]+'\n'+'让球返还率'+'\n'+item['Bet365让球返还率'][0]+'\n'+item['Bet365让球返还率'][1], e,'返还率'+'\n'+ item['澳门返还率'][0]+'\n'+item['澳门返还率'][1]+'\n'+'让球返还率'+'\n'+item['澳门让球返还率'][0]+'\n'+item['澳门让球返还率'][1]]
            print(list_a)
            file.writerow(list_a)
        else:
            pass
        yield item


