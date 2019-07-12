import requests
import re
import json
import csv
url="http://db.auto.sohu.com/cxdata/xml/basic/modelList.xml"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
def get_id():
    res=requests.get(url,headers=headers).text
    item={}
    item['品牌']=re.findall('<model brandName="(.*?)"',res)
    item['车型']=re.findall('name="(.*?)"',res)
    item['id']=re.findall('id="(.*?)"',res)
    return item
def get_sale(id):
    item=get_id()
    url=f'http://db.auto.sohu.com/cxdata/xml/sales/model/model{id}sales.xml'
    res=requests.get(url,headers=headers).text
    item['时间']=re.findall('sales date="(.*?)"',res)
    item['销量']=re.findall('salesNum="(.*?)"',res)
    return item
def save_file(data):
    with open('aa.csv','a',encoding='utf-8') as f:
        cs=csv.writer(f)
        cs.writerow(data)
        # data=json.dumps(data,ensure_ascii=False)
        # f.write(data+'\n')
if __name__=='__main__':
    id=get_id()['id']
    for i in id:
        a=get_sale(i)
        for i in range(len(a['id'])):
            for j in range(len(a['时间'])):
                data=[a['品牌'][i],a['车型'][i],a['时间'][j],a['销量'][j]]
                print(data)
                save_file(data)