from bs4 import BeautifulSoup
import requests
import time


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


def get_info(url):  # 定义获取信息的函数
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    try:
        for rank, title, time0 in zip(ranks, titles, times):
            data = {
                'rank': rank.get_text().strip(),
                'singer': title.get_text().split('-')[0],
                'song': title.get_text().split('-')[1],  # 通过split()获取歌手和歌曲信息
                'time': time0.get_text().strip()
            }
            print(data)  # 获取爬虫信息并按字典格式打印
    except IndexError:
        pass


if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i))
            for i in range(1, 24)]  # 构建多页url
    for single_url in urls:
        # print(single_url)
        get_info(single_url)
        time.sleep(3)

