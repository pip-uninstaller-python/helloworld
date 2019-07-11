import requests
import redis
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
def get_detail(url):
    res=requests.get(url,headers=headers).json()
    data=res['data']
    return data
if __name__=='__main__':
    rs = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True,db=1)
    for i in range(20,60,20):
        url=f"https://www.zhihu.com/api/v4/members/ponyma/followers?offset={i}&limit=20"
        data=get_detail(url)
        for j in data:
            print(j)
            id=j['id']
            name=j['name']
            # use_default_avatar=j['use_default_avatar']
            rs.hset('message',id,name)

