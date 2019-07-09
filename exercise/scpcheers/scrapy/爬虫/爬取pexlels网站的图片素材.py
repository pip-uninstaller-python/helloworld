from bs4 import BeautifulSoup as bs
import requests
from multiprocessing import Pool
# article > a > img

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

picture_urls = []


def get_info_from(url):
    try:
        res = requests.get(url, headers=headers)
        soup = bs(res.text, 'lxml')
        imgs = soup.select('article > a > img')
        for img in imgs:
            photo = img.get('src')
            picture_urls.append(photo)
        path = 'F://test/photos/'
        for item in picture_urls:
            data = requests.get(item, headers=headers)
            fp = open(path + item.split('?')[0][-10:], 'wb')
            fp.write(data.content)  # 写入图片内容
            fp.close()  # 关闭文件
    except requests.exceptions.ConnectionError:
        pass


if __name__ == '__main__':
    urls = ['https://www.pexels.com/search/gym/?page={}'.format(str(i))
            for i in range(1, 10)]
    pool = Pool(processes=4)
    pool.map(get_info_from, urls)
