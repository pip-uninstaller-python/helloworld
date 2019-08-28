# -*- coding: utf-8 -*-
# Author xmcui

import requests
import json
import redis

# 连接redis 注意decode_responses一定要加,不然key和value都是bytes类型的类,处理起来非常麻烦
redis = redis.Redis('192.168.1.104', encoding='UTF-8',decode_responses=True)
# 定义redis的key
hashKey = 'tx_news_hash'
listKey = 'tx_news_list'

# 获取滚动新闻的标题和链接,把这些信息存入Redis
def get_page_url(date, num, page):
    print(date, num, page)
    result = requests.get(
        'https://pacaio.match.qq.com/openapi/json?key=news:%d&num=%d&page=%d&expIds=&callback=__jp0' % (date, num, page))
    # 得到的返回值被故意加了一层,把这一层切掉才是json的标准格式
    j = json.loads(result.text[6:-1])
    # 页数超过最后一页后,没有数据,直接跳出返回False停止下一页请求
    if j['data'] == None:
        return False
    # 得到正常返回值后遍历所有'data'节点
    for jj in j['data']:
        title = jj['title']
        url = jj['url']
        print(title,url)
        # 判断redis是否已经存在该文章标题,如果不存在,将它加进Redis中
        if not redis.hexists(hashKey, title):
            # 使用Hash是为了防止加入重复数据
            # List是起到消息队列的作用,消费者从队列右侧pop即可
            redis.hset(hashKey, title, url)
            redis.lpush(listKey,title)
        # 如果标题已经存在,有可能是以下情况:
        #   1. 在之前已经爬过这一天数据了,数据没有更新
        #   2. 在之前爬过这一天数据了,数据更新了,但是之前的循环已经把更新的数据搞定了
        # 这两种情况中,无论剩下的还是后面页的所有数据都已经存入Redis了,所以直接跳出并且终止下一页的请求
        else:
            return False
    # 本页数据都存成功了,请求下一页
    return True

# 之所以提出来用循环而不用迭代是为了防止爆栈
def get_day_url(date):
    nextPageExist = True
    i = 0
    while nextPageExist:
        nextPageExist = get_page_url(date, 15, i)
        print('nextPageExist =',nextPageExist)
        i = i + 1

# 开始把今天新闻的url存入Redis
get_day_url(20190723)
