# from multiprocessing import Pool
# pool = Pool(processes==4)  # 创建线程池
# pool.map(func, iterable[, chunksize])

import requests
import re
import time
from multiprocessing import Pool

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}  # 定义请求头


def re_scraper(url):
    html = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', html.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',
                          html.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(.*?)</i> 好笑</span>',
                        html.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',
                          html.text, re.S)
    # for id, content, laugh, comment in zip(ids, contents, laughs, comments):
    #     print(id.strip(), content.strip(), laugh.strip(), comment.strip())
    for id, content, laugh, comment in zip(ids, contents, laughs, comments):
        info = {
            'id': id,
            'content': content,
            'laugh': laugh,
            'comment': comment
        }
        return info


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i))
            for i in range(1, 36)]
    start_1 = time.time()
    for url in urls:
        re_scraper(url)  # 单进程
    end_1 = time.time()
    print('串行爬虫用时:', end_1-start_1)
    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(re_scraper, urls)
    end_2 = time.time()
    print('两个进程用时：', end_2-start_2)
    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper, urls)
    end_3 = time.time()
    print('四个进程用时：', end_3-start_3)

