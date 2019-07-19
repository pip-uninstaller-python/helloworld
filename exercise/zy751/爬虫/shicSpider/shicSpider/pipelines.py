# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShicspiderPipeline(object):
    def process_item(self, item, spider):
        return item
class mysqlpipline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='root',db='mydb', port=3306, charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        self.cursor.execute("insert into info (title,phone,QQ,weixin) values(%s,%s,%s,%s)",(item['title'], item['phone'],item['QQ'],item['weixin']))
        self.conn.commit()
        return item
    def spider_close(self, spider):
        self.cursor.close()
        self.conn.close()


