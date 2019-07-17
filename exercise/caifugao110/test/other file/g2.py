import re
from urllib import request

class Spider():
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class= "txt">'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        try:
            print(root_html[0])
        except Exception as e:
            print(e)

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.go()

