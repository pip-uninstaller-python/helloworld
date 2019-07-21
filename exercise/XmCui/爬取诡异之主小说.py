# -*- coding: utf-8 -*-
#Author xmcui

import requests
from pyquery import PyQuery as q


def getPageText(base_url,next_page):
    result = requests.get(base_url+next_page)
    result.encoding = 'UTF-8'
    t = q(result.text)
    title = t('div.zhong').text()
    print(title)
    text = t('article#nr').text()
    # TODO 在这里持久化
    serializeToFile('D:\myCode\python\crawler\gyzz.txt',title,text)
    exist_next_page=False
    for aa in t('a.dise'):
        if aa.text=='下一页' :
            next_page=q(aa).attr.href
            print(next_page)
            exist_next_page=True
            break

    if not exist_next_page :
        return

    getPageText(base_url,next_page)

def serializeToFile(file,title,text):
    with open(file,'a+',encoding='UTF-8') as f:

        f.write(title+'\n\n'+text)

getPageText('https://m.biquge.info','/3_3746/1992425.html')


