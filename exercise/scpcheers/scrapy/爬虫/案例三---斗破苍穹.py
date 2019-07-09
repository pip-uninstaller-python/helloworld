import requests
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


f = open('F:/file.txt', 'a+')  # 打开txt文档，追加的方式


def get_info(url):  # 定义获取信息的函数
    res = requests.get(url, headers=headers)
    if res.status_code == 200:  # 判断请求码是否为200
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)
        for content in contents:
            f.write(content+'\n')  # 正则获取数据写入txt文档中
    else:
        pass  # 不为200就pass掉


if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i))
            for i in range(2, 1665)]  # 构造多页url
    for single_url in urls:
        print(single_url)
        get_info(single_url)
        time.sleep(1)
    f.close()  # 关闭文件

