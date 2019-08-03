# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  pymysql
from lvmaSpider.settings import *
class LvmaspiderPipeline(object):
    def process_item(self, item, spider):
        return item
class mysqlpipline(object):
    def __init__(self):
        self.conn=pymysql.Connect(host='localhost',user='root',password='root',db='mydb',charset='utf8',port=3306)
        self.cursor=self.conn.cursor()
        start=f"DROP TABLE  IF EXISTS {STR}"
        self.cursor.execute(start)
        if STR=='跟团游'or STR=='自由行'or STR=='当地游'or STR=='酒店景点':
            sql=f'''create table {STR} (href varchar(255),price varchar(255),days varchar(255),title varchar(255),tuij varchar(255),process varchar(255));'''
        if STR == '景点门票':
            sql = f'''create table {STR} (price varchar(255),type varchar(255),url varchar(255),place varchar(255));'''
        if STR == '酒店':
            sql = f'''create table {STR} (href varchar(255),name varchar(255),surrounding varchar(255),address varchar(255),start varchar(255),price varchar(255));'''
        if STR=='机票':
            sql=f'''create table {STR} (href varchar(255),name varchar(255),starttime varchar(255),time varchar(255),endtime varchar(255),price varchar(255));'''
        self.cursor.execute(sql)
    def process_item(self, item, spider):
        if STR=='跟团游'or STR=='自由行'or STR=='当地游'or STR=='酒店景点':
            sql=f'insert into {STR}  values(%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql,(item['href'],item['price'],item['days'],item['title'],item['tuij'],item['process']))
        if STR=='酒店':
            sql = f'insert into {STR}  values(%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql,(item['href'],item['name'],item['surrounding'],item['address'],item['start'],item['price']))
        if STR=='景点门票':
            sql = f'insert into {STR}  values(%s,%s,%s,%s)'
            self.cursor.execute(sql,(item['price'],item['type'],item['url'],item['place']))
        if STR=='机票':
            sql = f'insert into {STR}  values(%s,%s,%s,%s,%s,%s)'
            self.cursor.execute(sql,(item['url'],item['name'],item['starttime'],item['time'],item['endtime'],item['price']))
        self.conn.commit()
        return item
    def spider_close(self):
        self.cursor.close()
        self.conn.close()