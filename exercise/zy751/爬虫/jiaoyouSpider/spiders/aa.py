# -*- coding: utf-8 -*-
import scrapy
import json


class AaSpider(scrapy.Spider):
    name = 'aa'
    allowed_domains = ['7799520.com']
    start_urls = [f'http://www.7799520.com/api/user/pc/list/search?marry=1&page={i}' for i in range(10)]

    def parse(self, response):
        # print('*'*80)
        # print(response.request.headers)
        # print('*' * 80)
        data_list=json.loads(response.text)
        if data_list.get('data',False):
            if data_list['data'].get('list',False):
                for data in data_list['data']['list']:
                    image=data.get('avatar',False)
                    item={
                        'image':image
                    }
                    yield item