
import json
import re
def get_headrs():#该函数实现将带冒号的字符串改成字典
#下面为要分割的字符串
    headers_str = """Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 26
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _ga=GA1.2.1240643066.1540209044; user_trace_token=20181022195043-b4f35172-d5f0-11e8-977d-525400f775ce; LGUID=20181022195043-b4f35434-d5f0-11e8-977d-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166ebeb76562b8-0fce0a466e86c9-36664c08-1049088-166ebeb765710%22%2C%22%24device_id%22%3A%22166ebeb76562b8-0fce0a466e86c9-36664c08-1049088-166ebeb765710%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAIAACBIF249A8B614163CBF10D4CEEB7CA8EA1D; _gid=GA1.2.75812891.1561040124; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558960543,1559392521,1559998801,1561040125; LGSID=20190621212247-a92d871d-9427-11e9-a442-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; SEARCH_ID=d07219ff73c14be5888645ee13a50d6c; X_HTTP_TOKEN=010cabdaca147f5d47332116515e2327bd48e181a6; LGRID=20190621212255-adefbffb-9427-11e9-b4c3-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1561123376; TG-TRACK-CODE=search_code
Host: www.lagou.com
Origin: https://www.lagou.com
Referer: https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36
X-Anit-Forge-Code: 0
X-Anit-Forge-Token: None
X-Requested-With: XMLHttpRequest
"""


    pattern = '^(.*?): (.*)$' #正则表达式模板
    #              1     2
    dict={}
    for line in headers_str.splitlines():#将字符串以行分割并遍历每一行
        print(line.split(":"))#j将字符串按：分隔开
        dict[line.split(":")[0]]=line.split(":")[1]#通过直接赋值形成字典
    return dict
headers=get_headrs()
print(headers)

