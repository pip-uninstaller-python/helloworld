import requests
import os
import datetime
from bs4 import BeautifulSoup
def get(url):#获取网页源码信息
    try:
        r=requests.get(url)
        r.encoding=r.apparent_encoding#设置编码格式为网页编码格式
        return r.text
    except:
        return ''
def parse(text,html):
    page=BeautifulSoup(html,'html.parser')
    lis=page.find_all('li',class_='title')
    for i in lis:
        text.append(i.a.string)
def findpage(html):
    page = BeautifulSoup(html, 'html.parser')
    lis=page.find('ul',class_='yk-pages')
    lilist=[]
    for li in lis:
        lilist.append(li)
    length=lilist[-2].string
    return length
def printnamelist(html,trueyear,show):
    if not os.path.exists(r'C:\Users\Public\优酷爬取信息'):#创建文件夹存储类别信息
        os.mkdir(r'C:\Users\Public\优酷爬取信息')
    if not os.path.exists(r'C:\Users\Public\优酷爬取信息\{0}'.format(show)):#创建类别文件夹
        os.mkdir(r'C:\Users\Public\优酷爬取信息\{0}'.format(show))
    path=r'C:\Users\Public\优酷爬取信息\{0}\{1}.txt'.format(show,trueyear)#在类别文件夹中分年份存储信息
    list=open(path,'w',encoding='utf-8')#在年份文件夹内写入
    list.write(str(trueyear)+'年全部{}节目'.format(show)+'\n')
    for i in range(len(html)):#标号写入
        list.write(str(i+1)+'.'+html[i]+'\n')
    list.close()
    return ''
def main():
    year = 2019#设置当前年份
    starttime=datetime.datetime.now()#获取当前时间
    print('有以下优酷类别你可以爬取：动漫，体育，电影')
    category={'动漫':'100','电影''':'96','体育':'98'}#这是看每个类别对应的数字 方便构建网址
    show=input("请输入你要爬取的:")
    url1 = 'http://list.youku.com/category/show/c_'
    url2='_r_'
    url3 = '_s_1_d_1_p_'
    url4 = '.html?spm=a2h1n.8251845.0.0'
    num=int(input("请输入你要爬取几年的："))#设置爬取年份
    while num > 0:
        namelist = []
        trueyear = year - num + 1#
        # 下面的三句话都是为了获取每一个类别每一年有多少页码
        turl = url1 + category[show] + url2 + str(trueyear) + url3 + str(1) + url4
        thtml = get(turl)
        length = int(findpage(thtml))
        # print(str(trueyear)+"有"+str(length)+"页")
        for i in range(1, length + 1):
            url = url1 + category[show] + url2 + str(trueyear) + url3 + str(i) + url4
            # print(url)
            # print("这是{0}年第{1}页的内容".format(trueyear,i))
            html = get(url)
            parse(namelist, html)
        printnamelist(namelist, trueyear, show)
        num = num - 1
    endtime = datetime.datetime.now()
    print("运行时间为：{}".format(endtime - starttime))
main()



