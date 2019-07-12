import urllib.request
import requests
header = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    'Cookie': 'bid=DIuSbFmd4Bc; gr_user_id=468b0254-0097-48d9-9509-f4051b94654b; _vwo_uuid_v2=DA2CBBE054B6FD78A3AFFFFCFD00166BE|5abfa9f217b791c41bd539f562fdb697; __utmc=30149280; viewed="4913064_26715115_27047716_3709579"; ll="108296"; __utmc=223695111; __utmz=223695111.1548147477.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=w5x514Fu0dWPMelpsRLCWmYT66wtierL; ct=y; douban-fav-remind=1; __utmz=30149280.1548148474.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.81298697.1548056652.1548148474.1548153828.5; __utma=223695111.710364214.1548147477.1548147477.1548153828.2; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1548209652%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=f4f89b9a00fa963e.1548147477.3.1548209652.1548154421.; _pk_ses.100001.4cf6=*',
    "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
proxies = {
 "http": "http://10.10.1.10:3128",
 "https": "http://10.10.1.10:1080",
}
requests.get('https://movie.douban.com/j/search_subjects?'
                        'type=tv&tag=%E7%BA%AA%E5%BD%95%E7%89%87&sort=recommend&page_limit=10&page_start=1',proxies=proxies,headers=header)

