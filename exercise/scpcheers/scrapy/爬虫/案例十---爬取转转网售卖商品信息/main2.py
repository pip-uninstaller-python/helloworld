# 实现断点续爬
# 通过另个数据集合的url集合相减得到还未录入的url


# import sys
# sys.path.append('..')
# from multiprocessing import Pool
#
#
# db_urls = [item['url'] for item in tongvhrng_url.find()]
# db_infos = [item['url'] for item in tongvhrng_info.find()]
#
# x = set(db_urls)
# y = set(db_infos)
# rest_urls = x-y
#
# if __name__ == '__main__':
#     pool = Pool(processes=4)
#     pool.map(get_info, rest_urls)

