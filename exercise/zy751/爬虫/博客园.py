import requests
import re
def post(str):
    session=requests.Session()
    #url="https://www.cnblogs.com/mvc/PostComment/Add.aspx"
    url='https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fhome.cnblogs.com%2Fblog%2F'
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
    res=session.get(url,headers=headers)
    token=re.search('name=__RequestVerificationToken type=hidden value=(.*?)>',res.text)[1]
    print(token)
    key=re.search('name=PublicKey value=(.*?)>',res.text)[1]
    print(key)
    data1={
        'LoginName':'zy123451',
        'Password':'zy415320.',
        '__RequestVerificationToken':token,
        'PublicKey':key
    }
    session.post(url,headers=headers,data=data1)

    data={
    'blogApp':"xiaoxiaotank",
    'body':str,
    'parentCommentId':'0',
    'postId':'11078571'
    }
    cookie={
    "cookie":"_ga=GA1.2.158148253.1558313715; __gads=ID=2043acc179f4021b:T=1558313717:S=ALNI_MYgVO4530KXKAD9xjm_j-KTRR2Wlg; _gid=GA1.2.589494181.1562637111; .Cnblogs.AspNetCore.Cookies=CfDJ8D8Q4oM3DPZMgpKI1MnYlrlW4lTc59EvgWOGRw7qH00UJpXPH0E-YVENWsf0ULemiPSzMMhfz04A8ndbfiUBTt5DOAiaTKilh7AgZe0PIw45E_pOEim9YOy2V-kV64U18T-QGkcqWVGCtAGQFC3SgnCtYqbYqsvrJaUCfkkHeKkgEVIbNHWX3mExbVM7XfbUyMHjyr4nPSLAh8cXkhHFM6S_JX8wnoQIIXAV0g3E24YGgTJVPDUtItrhadprWB9vx2APQRCd_JRogM1ZqVOwHaM7AfGRh-TeyGxHX4Dkj07xcLx1KJIykA--lnlul0-1h1ysW8IRSiGER2YJdWjsd_Hqgpl_g9eubSfgRqeeh4-n5k6JGZRyQyCY5ZEEoNln_Pn31irPsrppNsavByLarFbH_RLboie_SGWzoLovriu814kATjX6M39jc_e76keJ3A; .CNBlogsCookie=41BDBE3C536D3FB0AD9CDB403AE27910026F844DD834B6A31EF2154CE046DB784D0ECF43E797C955DA44B8B5707AD0366C80E7092FAA258AD761E874CD52AF80A42620426B53861431CF4C3F165FA033731352F6; _gat=1"
    }
    aaurl = "https://www.cnblogs.com/mvc/PostComment/Add.aspx"
    a=requests.post(aaurl,data=data,cookies=cookie,headers=headers)
    print(a.json())
post('aaaaa')