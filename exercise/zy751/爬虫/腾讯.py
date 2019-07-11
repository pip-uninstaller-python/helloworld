import requests
import json
import csv
def get_data(index):
    url="https://careers.tencent.com/tencentcareer/api/post/Query"
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    data={
        "timestamp":"1561901284758",
        "pageIndex":index,
        "pageSize":"10",
    }
    res=requests.get(url,params=data,headers=headers).json()
    datalist=res['Data']['Posts']
    for i in range(10):
        RecruitPostName=datalist[i]['RecruitPostName']
        Responsibility=datalist[i]['Responsibility']
        item=[RecruitPostName,Responsibility]
        yield item
def save_csv(i):
  with open('aa.csv', 'a', encoding='utf-8')as f:
            a = csv.writer(f)
            a.writerow(i)

for i in range(10):
    data=get_data(i)
    for i in data:
        save_csv(i)