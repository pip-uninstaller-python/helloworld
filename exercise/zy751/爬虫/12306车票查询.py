import requests
from prettytable import PrettyTable
import re

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie':'BIGipServerpool_index=804258314.43286.0000; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=317719050.50210.0000; RAIL_EXPIRATION=1567899267939; RAIL_DEVICEID=YBQySsXrI3vt3tmdQ4gijKqZEJFBxbgffZM9uA6pfR_gbpj_R6V8LCA4NDfccu1ChpoLDSSgs1yqf9eNazXAgtY1uQnRyslSOW8sLORrXwYawkSOeVOZT6yD7XSPMJx1wwR8QvvN-71fuIL496qoTH8cg5YkZiBS',
}
def get_station():
    url='https://www.12306.cn/index/script/core/common/station_name_v10036.js'
    res=requests.get(url,headers=headers)
    re1=re.sub("var station_names ='",'',res.text)
    re1=re.sub('\d{0,3}@.*?\|','',re1)
    result=re1.split('|')
    # print(result)
    return result
def jianhua(list):
    l1=[]
    l2=[]
    dict={}
    for i in range(0,len(list),2):
        l1.append(list[i])
    for j in range(1,len(list),2):
        l2.append(list[j])
    l1=l1[:-1]
    for i in range(len(l1)):
        name=l1[i]
        dict[name]=l2[i]
    return dict

def get_data(url):
    res=requests.get(url,headers=headers)
    data=res.json()['data']['result']
    for i in data:
        i=i.split('|')
        checi=i[3]
        start=i[8]
        time=i[10]
        end=i[9]
        sw=i[32]
        yd=i[31]
        rw=i[23]
        yw=i[26]
        wuzuo =i[28]
        ed = i[30]
        yz = i[29]
        result.append([checi,start,end,time,sw,yd,ed,yz,yw,rw,wuzuo])
def show_table():
    table=PrettyTable(["车次","发车时间","到达时间",'耗时',"商务座","一等座","二等座","硬座","硬卧","软卧","无座"])
    for i in  result:
        table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]])
    print(table)
if __name__=='__main__':
    result = []
    list = get_station()
    dict=jianhua(list)
    # print(dict)
    starts=dict[input('请输入起始站：')]
    ends=dict[input('请输入目的地：')]
    day=input('请输入出发日期：（格式2019-08-20）')
    url = f'https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={day}&leftTicketDTO.from_station={starts}&leftTicketDTO.to_station={ends}&purpose_codes=ADULT'
    # print(url)
    get_data(url)
    show_table()