import requests
import json
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
def get_detail(page):
    url="http://www.7799520.com/api/user/pc/list/search?marry=1&page={}".format(page)#实现翻页
    r=requests.get(url,headers=headers).json()
    data=r['data']['list']#获取列表信息
    for i in data:#获取列表中每个人的信息并写入
        with open('良缘.txt','a') as f:
            data=json.dumps(i,ensure_ascii=False)
            f.write(data+'\n')
for i in range(10):
    get_detail(i)
