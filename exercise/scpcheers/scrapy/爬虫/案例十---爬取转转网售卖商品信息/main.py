import sys
sys.path.append('..')
from multiprocessing import Pool
from get_url import get_class_urls, get_class_detail_url, start_url
from page_spider import get_info_from


def get_all_links_from(class_url):
    for i in range(1, 2):  # 广度遍历 控制页面数 重复数据使用pandas清洗
        urls = get_class_detail_url(class_url, i)
        get_info_from(urls)


if __name__ == '__main__':
    class_urls = get_class_urls(start_url)
    pool = Pool(processes=4)  # 创建进程池
    pool.map(get_all_links_from, class_urls)

