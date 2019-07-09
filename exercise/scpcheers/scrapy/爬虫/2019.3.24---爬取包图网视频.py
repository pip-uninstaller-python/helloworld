import requests
from lxml import etree


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}   # 加入请求头


class Spider(object):
    def start_request(self):
        # 1.发送请求  包图网整体数据
        # urls = ['https://ibaotu.com/shipin/7-0-0-0-0-{}.html'.format(str(i))
        #                         for i in range(1, 3)]
        response = requests.get('https://ibaotu.com/shipin/7-0-0-0-0-3.html', headers=headers)
        # test
        # print(response.text) # 保存为xml文本，后续对想你了解析
        self.xpath_data(response)

    def xpath_data(self, response):
        # 2.抽取数据，视频标题、视频链接
        xml = etree.HTML(response.text)
        title_list = xml.xpath('//span[@class="video-title"]/text()')
        video_list = xml.xpath('//div[@class="video-play"]/video/@src')
        # 测试数据
        # for x, y in zip(title_list, video_list):
        #     print(x, y)
        self.with_file(title_list, video_list)

    def with_file(self, title_list, video_list):
        # 3.补全视频url
        video_urls_list = video_list
        for video_url, title in zip(video_urls_list, title_list):
            video_url = "http:" + video_url
            video = requests.get(video_url)  # 发送请求

            filename = title + ".mp4"  # 定义文件名
            path = 'F://vedio/'
            print('正在保存视频：' + filename)  # 存储路径
            with open(path + filename, 'wb') as f:
                f.write(video.content)


spider = Spider()
spider.start_request()

