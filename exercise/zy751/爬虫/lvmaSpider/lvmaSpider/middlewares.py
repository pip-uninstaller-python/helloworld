# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse


class LvmaspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LvmaspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class seleniumMI(object):
    def __init__(self):
        self.browser=webdriver.Chrome()

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()  # 实例化
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s
    def process_request(self, request, spider):
        a = request.meta.get('sele', False)
        if a:
            self.browser.get(request.url)
            start = self.browser.find_element_by_id('deptCity')
            kaishi = input('请输入你的出发站')
            start.clear()
            start.send_keys(f'{kaishi}')
            final = self.browser.find_element_by_id('arrvCity')
            jieshu = input('请输入你的终点站')
            final.send_keys(f'{jieshu}')
            days = self.browser.find_element_by_id('goDate')
            days.click()
            str = input('请输入你出发时间,格式为当前日期格式')
            kexuan = self.browser.find_element_by_xpath(f'//td[@data-date-map="{str}"]')
            kexuan.click()
            search = self.browser.find_element_by_partial_link_text('搜')
            search.click()
            response=HtmlResponse(url=self.browser.current_url,
                                           body=self.browser.page_source,
                                           encoding="utf-8",
                                           request=request)
            return response
    def spider_closed(self):
        self.browser.quit()
