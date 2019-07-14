# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import csv


class TenxunspiderPipeline(object):
    def process_item(self, item, spider):
        return item
class jsonPipine(object):
    def __init__(self):
        self.file=codecs.open('bb.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        line=json.dumps(item['message'],ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def spider_close(self,spider):
        self.file.close()
a=1
class csvpipline(object):
    def __init__(self):
        self.file=open('aa.csv','w',encoding='utf-8',newline='')
        self.a = csv.writer(self.file)
    def process_item(self,item,spider):
        global a
        while a>0:
            self.a.writerow([i for i in item['message']])
            a-=1
        self.a.writerow([item['message'][i] for i in item['message']])
        return item
    def spider_close(self,spider):
        self.file.close()