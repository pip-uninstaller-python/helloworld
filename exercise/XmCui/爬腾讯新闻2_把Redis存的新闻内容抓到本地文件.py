# -*- coding: utf-8 -*-
# Author xmcui
from json import JSONDecodeError

import requests
import redis
import os
import json
from pyquery import PyQuery as q


# 消费Redis中的数据
def redis_consumer(listKey, hashKey, redis):
    while True:
        # 一直不停从Redis的List中取数据,直到取空
        title = redis.rpop(listKey)
        if title == None:
            return
        # 拿到标题后,根据标题拿到url
        url = redis.hget(hashKey, title)
        print(url)
        t = get_page_info(url)
        # 定义储存文件的目录
        dirS = 'D:/myCode/python/crawler/news/'
        # 调用序列化方法
        file=serialize_to_file(dirS, title+'.txt', t)
        print("输出文件:"+file)


# 根据url抓页面信息
def get_page_info(url):
    t = ''
    # 获取页面信息
    re = requests.get(url)
    # 使用pyqyery解析得到标题和内容
    info = q(re.text)
    # 获取标题
    title = info('body > div.qq_conent.clearfix > div.LEFT > h1').text()
    t += title + '\n\n'+url +'\n'
    # 我发现页面js中含有一个json串,含有新闻的基本信息,切片获取后用json解析
    # 获取js语句,切片后得到json串
    aaa = info('head > script:last').text()[14:]
    try:
        j = json.loads(aaa, encoding='UTF-8')
    except JSONDecodeError as e :
        print(e)
    # 发表媒体
    media = j['media']
    t += '作者:' + media + '\n'
    # 发布时间
    pubtime = j['pubtime']
    t += '发布时间:' + pubtime + '\n'
    # 新闻标签
    tags = j['tags']
    t += '关键字:' + tags + '\n\n'
    # 新闻内容
    ps = info('body > div.qq_conent.clearfix > div.LEFT > div.content.clearfix > div.content-article > p')
    for p in ps:
        # 每次一段
        t +=q(p).text()
        t +='\n\n'
    return t


# 把数据序列化到文件中
def serialize_to_file(dir, file_name, info):
    # 看下目录存在不,如果不存在就创建一个
    if not os.path.exists(dir):
        os.mkdir(dir)
    # 以新闻题目为文件名,写入文件
    with open(dir+file_name, 'w+', encoding='UTF-8') as f:
        f.write(info)
        return dir + file_name

# 连接Redis 注意decode_responses一定要加,不然key和value都是bytes类型的类,处理起来非常麻烦
redis = redis.Redis('192.168.1.104', encoding='UTF-8', decode_responses=True)
# 启动
redis_consumer('tx_news_list', 'tx_news_hash', redis)
