# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
import re
from urllib.parse import unquote
from ..settings import *

class LvmaSpider(scrapy.Spider):
    name = 'lvma'
    allowed_domains = ['lvmama.com']
    start_urls = ['http://lvmama.com/']
    def parse(self, response):
        '''爬取三种类型的旅游及其相关网址，并选择一种访问'''
        if STR=='机票':
            yield scrapy.Request(
                'http://flight.lvmama.com/',
                callback=self.parse_ji,
                meta={'sele':True}
            )

        if STR=='酒店':
            name_list=response.xpath('//div[@class="lv_s_hot"]/dl/dd/a/@href').getall()
            for i in name_list:
                print(i)
                yield scrapy.Request(
                    i,
                    callback=self.parse_jiu,
                )

        if STR=='景点门票':
            href_list=response.xpath('//div[@class="lv_s_r"]/div[@class="lv_s_list"][1]//div[@class="lv_s_hot_list"]/dl/dd/a/@href').getall()
            place_list=response.xpath('//div[@class="lv_s_r"]/div[@class="lv_s_list"][1]//div[@class="lv_s_hot_list"]/dl/dd/a/text()').getall()
            if href_list:
                for i,j in zip(href_list[:8],place_list[:8]):
                    if j=='芜湖方特':
                        yield scrapy.Request(
                            i,
                            callback=self.parse_wuhu,
                        )

                    else:
                        yield scrapy.Request(
                            i,
                            callback=self.parse_jing,
                            meta={'url':i,'j':j}
                        )

        if STR=='酒店景点':
            href_list = response.xpath('//div[@class="lv_s_r"]/div[@class="lv_s_list"][1]//div[@class="lv_s_hot_list"]/dl/dd/a/@href').getall()
            place_list = response.xpath('//div[@class="lv_s_r"]/div[@class="lv_s_list"][1]//div[@class="lv_s_hot_list"]/dl/dd/a/text()').getall()
            for i,j in zip(href_list[8:],place_list[8:]):
                yield scrapy.Request(
                    i,
                    callback=self.parse_jiudian,
                    meta={'url':i}
                )

        if STR=='跟团游':
            href_list=response.xpath('//div[@class="lv_s_list lv_s_group"]//div[@class="lv_s_hot_list"]/dl/dd/a/@href').getall()
            if href_list:
                for i in href_list:
                    yield scrapy.Request(
                        i,
                        callback=self.next_page,
                        meta={'url':i}
                    )

        if STR=='自由行':
            href_list=response.xpath('//div[@class="lv_s_r"]/div[@class="lv_s_list"][2]//div[@class="lv_s_hot_list"]/dl/dd/a/@href').getall()
            if  href_list:
                for i in href_list:
                    yield scrapy.Request(
                        i,
                        callback=self.next_page2,
                        meta = {'url':i}
                    )

        if STR == '当地游':
            href_list = response.xpath('//div[@class="lv_s_hot_list hasRecom"]/dl/dd/a/@href').getall()
            if href_list:
                for i in href_list:
                        yield scrapy.Request(
                            i,
                            callback=self.next_page3,
                            meta={'url':i}
                        )
    def next_page(self,response):#
        '''跟团游翻页处理*'''
        furl = response.meta.get('url', False)
        try:
            sum = int(response.xpath('//span[@class="gopage"]/input/@totalpagenum').get())
            if re.search('zhangjiajie', furl) is not None:
                for i in range(1, sum + 1):
                    url = re.sub('H9', f'H9P{i}', furl)
                    yield scrapy.Request(
                        url,
                        callback=self.parse_gen,
                    )
            else:
                for i in range(1, sum + 1):
                    url = re.sub('#list', '&tabType=group', furl)
                    url = re.sub('\?', f'P{i}?', url)
                    yield scrapy.Request(
                        url,
                        callback=self.parse_gen,
                    )
        except:
            pass

    def next_page2(self,response):
        '''自由行翻页处理*'''
        furl = response.meta.get('url', False)
        sum = int(response.xpath('//span[@class="gopage"]/input/@totalpagenum').get())
        if re.search('ningbo', furl) is not None or re.search('sanya',furl) is not None:
            for i in range(1, sum + 1):
                url = re.sub('scenictour', f'scenictour-H80P{i}', furl)
                yield scrapy.Request(
                    url,
                    callback=self.parse_gen,
                )
        else:
            for i in range(1, sum + 1):
                url = re.sub('#list', '&tabType=scenictour', furl)
                url = re.sub('\?', f'P{i}?', url)
                yield scrapy.Request(
                    url,
                    callback=self.parse_gen,
                )
    def next_page3(self,response):
        '''当地游翻页处理*'''
        furl = response.meta.get('url', False)
        sum = int(response.xpath('//span[@class="gopage"]/input/@totalpagenum').get())
        for i in range(1, sum + 1):
            url = re.sub('#list\?losc=098027&ict=i|#list', '&tabType=localr', furl)
            url = re.sub('\?', f'P{i}?', url)
            yield scrapy.Request(
                url,
                callback=self.parse_gen,
            )
    def parse_wuhu(self,response):
        '''爬取景点门票时芜湖市是个特例打开后还要分模板'''
        href_list=response.xpath('//div[@class="product-section"]/h3/a/@href').getall()
        name_list=response.xpath('//div[@class="product-section"]/h3/a/@title').getall()
        for i,j in zip(href_list,name_list):
            yield scrapy.Request(
                i,
                callback=self.parse_jing,
                meta={'url':i,'j':j}
            )
    def parse_jing(self,response):
        '''爬取景点门票详情页内的所有框内信息'''
        info_list=response.xpath('//dl[@class="ptditem"]')
        url,place=response.meta.get('url'),response.meta.get('j')
        for i in info_list:
            price=''.join(i.xpath('.//dfn//text()').getall())
            type=' '.join(i.xpath('./dt[@class="pdname"]/a//text()').getall())
            type=re.sub(r'\s','',type)
            item={
                'price':price,
                'type':type,
                'url':url,
                'place':place
            }
            if item['price']=='':
                continue
            else:
                yield item
    def parse_jiudian(self,response):
        '''爬取酒店景点,实现翻页操作'''
        furl = response.meta.get('url', False)
        sum = int(response.xpath('//span[@class="gopage"]/input/@totalpagenum').get())
        if re.search('huangshan', furl) is not None:
            for i in range(1, sum + 1):
                url = re.sub('scenictour', f'scenictour-H80P{i}', furl)
                yield scrapy.Request(
                    url,
                    callback=self.parse_gen,
                )
        else:
            for i in range(1, sum + 1):
                url = re.sub('#list', '&tabType=scenictour', furl)
                url = re.sub('\?', f'P{i}?', url)
                yield scrapy.Request(
                    url,
                    callback=self.parse_gen,
                )
    def parse_gen(self,response):
        '''爬取当前页面的所有与旅游相关的网址还有相关内容'''
        info_list=response.xpath('//div[@class="product-list"]//div[@class="product-section"]/h3')
        for i in info_list:
            href=i.xpath('./a/@href').get()
            title=i.xpath('./a/span/@title').get()
            days=i.xpath('./a/span/em/text()').get()
            if days is None:
                try:
                    day= i.xpath('./a/span/@title').get()
                    days=re.findall('\d+天\d+晚|\d+日\d+晚',day)[0]
                except:
                    days=None
            tuij=i.xpath('../div[@class="pm-recommend"]/span/text()').get()
            if tuij:
                tuij=re.sub(r'\s','-',tuij)
            process=i.xpath('..//div[@class="product-ticket-dropdown"]/text()').get()
            if process:
                process = re.sub(r'\s', '', process)
            if process is None:
                try:
                    process=i.xpath('..//div[@class="product-detail-one-line"]/text()').get()
                    process=re.sub(r'\s','',process)
                except:
                    process=None
            price=i.xpath('../..//div[@class="product-price"]/em/text()').get().strip()
            item={
                'href':href,
                'title':title,
                'days':days,
                'tuij':tuij,
                'process':process,
                'price':price
            }
            yield item
    def parse_jiu(self,response):
        '''由于酒店跳转的页面不对,要在跳转后的页面重新找'''
        try:
            url=response.xpath('//a[text()="\r\n\t\t\t酒店\r\n\t\t\t"]/@href').get()
            print(url)
            yield scrapy.Request(
                url,
                callback=self.next_p,
                meta={'url':url}
            )
        except:
            pass
    def next_p(self,response):
        '''实现酒店页面的翻页操作'''
        furl=response.meta.get('url',False)
        try:
            sum = int(response.xpath('//div[@class="pagebox"]/a[last()-1]/text()').get())
        except:
            sum=1
        for i in range(1, sum + 1):
            url = re.sub('#list', '', furl)
            url = re.sub('\?', f'P{i}?', url)
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
            )
    def parse_detail(self,response):
        '''爬取酒店信息'''
        info_list=response.xpath('//dl[@class="proInfo"]')
        for i in info_list:
            name=i.xpath('./dt/a/text()').get()
            name=re.sub(r'\s','',name)
            href=i.xpath('./dt/a/@onclick').get()
            href=re.findall(r'http://.*?.html',href)[0]
            try:
                distance=''.join(i.xpath('./dd[2]//text()').getall())
                distance=re.sub(r'\s','',distance)
            except:
                distance=None
            try:
                address=i.xpath('./dd[3]/i/text()').get()
                address=re.sub(r'\s','',address)
            except:
                address=None
            try:
                start=i.xpath('./dd[4]/text()').get()
                start=re.sub(r'\s','',start)
            except:
                start=None
            price=''.join(i.xpath('../div//dfn//text()').getall())
            price=re.sub(r'\s','',price)
            item={
                'href':href,
                'name':name,
                'surrounding':distance,
                'address':address,
                'start':start,
                'price':price
            }
            yield item
    def parse_ji(self,response):
        '''航班信息爬取'''
        url=response.url
        flight_list=response.xpath('//div[@class="tl-detail clearfix"]')
        for info in flight_list:
            name=' '.join(info.xpath('./div[1]/div//text()').getall())
            name=re.sub(r'\s','',name)
            starttime=info.xpath('./div[2]/div/text()').get()
            starttime=re.sub(r'\s','',starttime)
            time=info.xpath('./div[3]/text()').get()
            time=re.sub(r'\s','',time)
            endtime=info.xpath('./div[4]/div/text()').get()
            endtime = re.sub(r'\s', '', endtime)
            price=''.join(info.xpath('./div[6]//text()').getall())
            price = re.sub(r'\s', '', price)
            item={
                'name':name,
                'starttime':starttime,
                'time':time,
                'endtime':endtime,
                'price':price,
                'url':url
            }
            print(item)
            yield item








