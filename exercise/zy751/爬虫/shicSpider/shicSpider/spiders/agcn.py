# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
from aip import AipOcr
APP_ID=	'16842100'
API_KEY = 'hvzTwGph2P927qkUCqj0GoNh'
SECRET_KEY = 'PgxDfsXlGj2dyiHhlFsMX1IxzUjIIVzb'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

class AgcnSpider(scrapy.Spider):
    name = 'agcn'
    allowed_domains = ['sgcn.com']
    start_urls = ['https://bbs.sgcn.com/forum.php?gid=1163']

    def parse(self, response):
        module_list=response.xpath('//tr//h2')
        dict={}
        for i in module_list:
            module=i.xpath('./a/text()').get()
            href=i.xpath('./a/@href').get()
            dict[module]=href
        print('你可以选择的有：')
        for i in dict:
            print(i,end=' ')
        print()
        str=input('请输入要爬取的板块')
        if str=='房产信息'or str=='房间出租':
            yield scrapy.Request(dict[str],
                                 callback=self.parse,
                                 )
        else:
            yield scrapy.Request(dict[str],
                                 callback=self.parse_detail)
    def parse_detail(self,response):
        data_list=response.xpath('//tbody[starts-with(@id,"normalthread_")]')
        for data in data_list:
            info=data.xpath('./tr/th/a[2]/text()').get()
            href=data.xpath('./tr/th/a[2]/@href').get()
            yield scrapy.Request(href,
                                 callback=self.parse_info,
                                 meta={'info':info})
        next_url=response.xpath('//a[text()="下一页"]/@href').get()
        if next_url:
            yield scrapy.Request(
                next_url,callback=self.parse_detail,
            )
    def parse_info(self,response):
        try:
            phone=response.xpath('//tr/th[text()="电话:"]/../td/text()').get()
            print(phone)
            if phone==None:
                print('无信息')
                return 1
            elif phone==' ':
                phone=response.xpath('// tr / th[text() = "电话:"] /../ td / img / @ src').get()
                phone=urljoin('https://bbs.sgcn.com/forum.php?gid=1163',phone)
                message = client.basicGeneralUrl(phone)
                for i in message.get('words_result'):
                    phone = i.get('words')
            qq=response.xpath('//tr/th[text()="QQ:"]/../td/text()').get()
            weixin = response.xpath('//tr/th[text()="微信:"]/../td/text()').get()
            item={
                'title':response.meta['info'],
                'phone':phone,
                'QQ':qq,
                'weixin':weixin
            }
            print(item)
            yield item
        except:
            pass
        # | // tr / th[text() = "电话:"] /../ td / img / @ src