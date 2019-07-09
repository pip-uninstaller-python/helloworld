import requests
import urllib.request
import re
import os
header={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
for i in range(1,10):#实现翻页的，该后面的数字可以爬取更多数据
    url="https://www.douyu.com/gapi/rknc/directory/yzRec/{}".format(i)
    r=requests.get(url,headers=header)
    text=r.text
    img=re.findall(r'"rs16":"(.*?)"',text)#抓取当前页面的所有图片地址
    name=re.findall(r'"nn":"(.*?)"',text)#抓取所有图片所有者的名字
    print(img)
    dict={}
    for a,b in zip(img,name):#这是个拉链函数，将a和b一一对应
        dict["图片"]=a
        dict["名字"]=b
        urllib.request.urlretrieve(url=dict["图片"],filename=r'C:\Users\Administrator\PycharmProjects\CODE\斗鱼图片\\'+'{}.png'.format(dict["名字"]))#需要更改你保存的路径
        print( dict)#打印输出结果，可以注释掉，上面已经保存了


  #  urllib.urlretrieve(img,'C:\Users\Administrator\PycharmProjects\CODE\斗鱼图片')

