# -*- coding: utf-8 -*-
import scrapy
import json


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = [f'https://www.zhihu.com/api/v4/members/ponyma/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={i*20}&limit=20' for i in range(10)]

    def parse(self, response):
        print('*'*80)
        print(response.request.headers)
        data_list=json.loads(response.text)
        if data_list.get('data',False):
            for data in data_list['data']:
                message=data
                print(message)
                item={
                    'message':message
                }
                yield item
