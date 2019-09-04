import requests
yzm_url='https://kyfw.12306.cn/passport/captcha/captcha-image'
check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
session=requests.session()
def get_yzmjpg(url):
    data={
        'login_site': 'E',
        'module': 'login',
        'rand': 'sjrand',
    }
    res=session.get(url,params=data)
    with open('yzm.jpg','wb') as f:
        f.write(res.content)
def check_jpg(url):
    answer=get_point(input('请输入验证码位置'))
    data={
        'answer': answer,
        'rand': 'sjrand',
        'login_site': 'E',
    }
    res=session.get(url,params=data)
    print(res.content.decode())
def get_point(index):
    indexs=index.split(',')
    list=[]
    for index in indexs:
        list.append(point_dict[index])
    list=','.join(list)
    return list
if __name__=="__main__":
    point_dict={
        '1':'40,45',
        '2':'116,53',
        '3': '185,52',
        '4':'257,50',
        '5':'40,121',
        '6':"116,133",
        '7':'185,132',
        '8':'257,130'
    }
    get_yzmjpg(yzm_url)
    check_jpg(check_url)
    res=session.get('https://www.12306.cn/index/index.html')
    print(res.content.decode())
